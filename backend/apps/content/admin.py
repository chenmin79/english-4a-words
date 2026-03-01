from django.contrib import admin

from .models import VocabWord, WordSet


@admin.register(WordSet)
class WordSetAdmin(admin.ModelAdmin):
    list_display = ("id", "key", "name", "version", "is_active", "created_at")
    list_filter = ("is_active", "version")
    search_fields = ("key", "name")


@admin.register(VocabWord)
class VocabWordAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "word_set", "unit", "pack_letter", "pos", "star", "sort_order")
    list_filter = ("word_set", "unit", "pack_letter", "star", "pos")
    search_fields = ("word", "chinese", "ex_en", "ex_zh")
    ordering = ("word_set", "sort_order", "id")
    autocomplete_fields = ("word_set",)

