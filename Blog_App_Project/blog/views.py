from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from rest_framework.exceptions import NotFound


from rest_framework import status
from rest_framework.response import Response



class PostMVS(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_user = self.request.user
        print(current_user)
        serializer.validated_data['author_id'] = current_user.id
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all().select_related('post')
    serializer_class = CommentSerializer


    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        if post_id == None:
            return self.queryset
        else:
            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                raise NotFound("A post with this id does not exist")
        return self.queryset.filter(post = post)


class LikeMVS(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer