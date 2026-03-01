from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import VocabWord, WordSet
from .serializers import VocabWordSerializer, WordSetSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def word_sets(request):
    qs = WordSet.objects.filter(is_active=True).annotate(word_count=Count("words")).order_by("key")
    return Response(WordSetSerializer(qs, many=True).data)


@api_view(["GET"])
@permission_classes([AllowAny])
def set_words(request, set_key):
    qs = VocabWord.objects.filter(word_set__key=set_key).order_by("sort_order", "id")
    return Response(VocabWordSerializer(qs, many=True).data)

