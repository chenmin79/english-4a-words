from django.db import transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.content.models import VocabWord, WordSet

from .models import StudySession, UserWordProgress
from .serializers import (
    ProgressBatchSerializer,
    StudySessionEndSerializer,
    StudySessionStartSerializer,
)


@api_view(["GET"])
def progress_by_set(request, set_key):
    rows = (
        UserWordProgress.objects.filter(user=request.user, word__word_set__key=set_key)
        .select_related("word")
        .all()
    )
    progress = {
        str(row.word_id): {
            "score": row.score,
            "next_review_at": row.next_review_at,
            "correct_count": row.correct_count,
            "wrong_count": row.wrong_count,
            "last_studied_at": row.last_studied_at,
        }
        for row in rows
    }
    return Response({"set_key": set_key, "progress": progress})


@api_view(["POST"])
def progress_batch(request):
    serializer = ProgressBatchSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    items = serializer.validated_data["items"]
    words = {w.id: w for w in VocabWord.objects.filter(id__in=[i["word_id"] for i in items])}
    now = timezone.now()

    with transaction.atomic():
        for item in items:
            word = words.get(item["word_id"])
            if word is None:
                continue
            obj, _ = UserWordProgress.objects.get_or_create(user=request.user, word=word, defaults={"score": 0})
            obj.score = item["score"]
            obj.next_review_at = item.get("next_review_at")
            obj.correct_count += item.get("correct_delta", 0)
            obj.wrong_count += item.get("wrong_delta", 0)
            obj.last_studied_at = now
            obj.save()

    return Response({"ok": True})


@api_view(["POST"])
def session_start(request):
    serializer = StudySessionStartSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    try:
        word_set = WordSet.objects.get(key=data["word_set_key"])
    except WordSet.DoesNotExist:
        return Response({"detail": "word set not found"}, status=status.HTTP_404_NOT_FOUND)

    session = StudySession.objects.create(
        user=request.user,
        word_set=word_set,
        pack_key=data["pack_key"],
        mode=data["mode"],
    )
    return Response({"session_id": session.id})


@api_view(["POST"])
def session_end(request):
    serializer = StudySessionEndSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    try:
        session = StudySession.objects.get(id=data["session_id"], user=request.user)
    except StudySession.DoesNotExist:
        return Response({"detail": "session not found"}, status=status.HTTP_404_NOT_FOUND)

    session.correct_count = data["correct_count"]
    session.wrong_count = data["wrong_count"]
    session.ended_at = timezone.now()
    session.save()
    return Response({"ok": True})

