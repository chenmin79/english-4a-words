from rest_framework import serializers

from .models import VocabWord, WordSet


class VocabWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabWord
        fields = [
            "id",
            "unit",
            "pack_letter",
            "word",
            "phonetic",
            "pos",
            "chinese",
            "ex_en",
            "ex_zh",
            "star",
            "sort_order",
        ]


class WordSetSerializer(serializers.ModelSerializer):
    word_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = WordSet
        fields = ["id", "key", "name", "version", "word_count"]

