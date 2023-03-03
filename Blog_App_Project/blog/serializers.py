from rest_framework import serializers
from .models import Post

import datetime


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    author_id = serializers.IntegerField()
    image = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = (
            'id',
            'image',
            'title',
            'content',
            'is_published',
            'created_date',
            'author',
            'author_id',
            'slug',
            
        )

    def get_created_date(self, obj):
        return datetime.datetime.strftime(obj.created_date, '%d,%m,%Y')