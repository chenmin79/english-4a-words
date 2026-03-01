from rest_framework import serializers


class ProgressBatchItemSerializer(serializers.Serializer):
    word_id = serializers.IntegerField()
    score = serializers.IntegerField(min_value=0, max_value=6)
    next_review_at = serializers.DateTimeField(required=False, allow_null=True)
    correct_delta = serializers.IntegerField(required=False, default=0, min_value=0)
    wrong_delta = serializers.IntegerField(required=False, default=0, min_value=0)


class ProgressBatchSerializer(serializers.Serializer):
    items = ProgressBatchItemSerializer(many=True)


class StudySessionStartSerializer(serializers.Serializer):
    word_set_key = serializers.CharField()
    pack_key = serializers.CharField()
    mode = serializers.ChoiceField(choices=["A", "B", "C"])


class StudySessionEndSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    correct_count = serializers.IntegerField(min_value=0)
    wrong_count = serializers.IntegerField(min_value=0)

