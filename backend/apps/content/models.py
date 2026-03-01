from django.db import models


class WordSet(models.Model):
    key = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=32, default="2024")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.key} - {self.name}"


class VocabWord(models.Model):
    word_set = models.ForeignKey(WordSet, on_delete=models.CASCADE, related_name="words")
    unit = models.PositiveIntegerField(null=True, blank=True)
    pack_letter = models.CharField(max_length=4, null=True, blank=True)
    word = models.CharField(max_length=100)
    phonetic = models.CharField(max_length=100, blank=True, default="")
    pos = models.CharField(max_length=20, blank=True, default="")
    chinese = models.CharField(max_length=200)
    ex_en = models.TextField(blank=True, default="")
    ex_zh = models.TextField(blank=True, default="")
    star = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [("word_set", "word")]
        indexes = [
            models.Index(fields=["word_set", "unit"]),
            models.Index(fields=["word_set", "pack_letter"]),
        ]

    def __str__(self):
        return self.word

