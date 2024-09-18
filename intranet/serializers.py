# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publish_year', 'description', 'category', 'image_url', 'video_url']


class RequestSerializer(serializers.Serializer):
    unique_id = serializers.CharField(max_length=50, allow_null=False, allow_blank=True)
    sentence_list = serializers.ListField(
        child=serializers.CharField(allow_blank=False, trim_whitespace=True)
    )