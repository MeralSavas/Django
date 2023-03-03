from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like


class PostMVS(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all().select_related('post')
    serializer_class = CommentSerializer

class LikeMVS(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer