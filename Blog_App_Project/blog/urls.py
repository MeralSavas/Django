from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostMVS, CommentMVS


router = DefaultRouter()

router.register('posts', PostMVS)
router.register('comments', CommentMVS)

urlpatterns = [
    path('', include(router.urls)),

]