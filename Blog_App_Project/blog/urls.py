from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostMVS, CommentMVS, LikeMVS


router = DefaultRouter()

router.register('posts', PostMVS)
router.register('comments', CommentMVS)
router.register('likes', LikeMVS)

urlpatterns = [
    path('', include(router.urls)),

]