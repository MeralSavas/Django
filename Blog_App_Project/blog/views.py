from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostMVS(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all().select_related('post')
    serializer_class = CommentSerializer