from django.conf import settings
from django.db import models

from apps.content.models import VocabWord, WordSet


class UserWordProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="word_progress")
    word = models.ForeignKey(VocabWord, on_delete=models.CASCADE, related_name="user_progress")
    score = models.IntegerField(default=0)
    next_review_at = models.DateTimeField(null=True, blank=True)
    correct_count = models.PositiveIntegerField(default=0)
    wrong_count = models.PositiveIntegerField(default=0)
    last_studied_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("user", "word")]
        indexes = [models.Index(fields=["user", "updated_at"])]


class StudySession(models.Model):
    MODE_CHOICES = [
        ("A", "Flashcard"),
        ("B", "Spell Check"),
        ("C", "Sentence Master"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="study_sessions")
    word_set = models.ForeignKey(WordSet, on_delete=models.CASCADE, related_name="study_sessions")
    pack_key = models.CharField(max_length=32)
    mode = models.CharField(max_length=1, choices=MODE_CHOICES)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    correct_count = models.PositiveIntegerField(default=0)
    wrong_count = models.PositiveIntegerField(default=0)

