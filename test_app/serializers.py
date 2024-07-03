from rest_framework import serializers


class PromptSerializer(serializers.Serializer):
    text = serializers.CharField()