import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.content.models import VocabWord, WordSet


class Command(BaseCommand):
    help = "Import vocabulary from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)
        parser.add_argument("--replace", action="store_true", help="Delete existing words before import")

    @transaction.atomic
    def handle(self, *args, **options):
        file_path = Path(options["json_file"])
        if not file_path.exists():
            raise CommandError(f"File not found: {file_path}")

        payload = json.loads(file_path.read_text(encoding="utf-8"))
        word_set, _ = WordSet.objects.get_or_create(
            key=payload["key"],
            defaults={
                "name": payload.get("name", payload["key"]),
                "version": payload.get("version", "2024"),
            },
        )
        word_set.name = payload.get("name", word_set.name)
        word_set.version = payload.get("version", word_set.version)
        word_set.save()

        if options["replace"]:
            VocabWord.objects.filter(word_set=word_set).delete()

        count = 0
        for idx, item in enumerate(payload.get("words", []), start=1):
            word = str(item.get("word", "")).strip()
            if not word:
                continue
            VocabWord.objects.update_or_create(
                word_set=word_set,
                word=word,
                defaults={
                    "unit": item.get("unit"),
                    "pack_letter": item.get("pack_letter"),
                    "phonetic": item.get("phonetic", ""),
                    "pos": item.get("pos", ""),
                    "chinese": item.get("chinese", ""),
                    "ex_en": item.get("ex_en", ""),
                    "ex_zh": item.get("ex_zh", ""),
                    "star": bool(item.get("star", False)),
                    "sort_order": item.get("sort_order", idx),
                },
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {count} words into {word_set.key}"))

