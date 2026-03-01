from django.contrib import admin

from .models import StudySession, UserWordProgress


@admin.register(UserWordProgress)
class UserWordProgressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "word", "score", "correct_count", "wrong_count", "last_studied_at", "updated_at")
    list_filter = ("score", "word__word_set")
    search_fields = ("user__username", "word__word", "word__chinese")
    autocomplete_fields = ("user", "word")


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "word_set", "pack_key", "mode", "started_at", "ended_at", "correct_count", "wrong_count")
    list_filter = ("word_set", "mode")
    search_fields = ("user__username", "pack_key")
    autocomplete_fields = ("user", "word_set")

