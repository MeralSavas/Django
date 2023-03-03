from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import PostMVS, CommentMVS, LikeMVS
from rest_framework_nested.routers import NestedSimpleRouter

router = SimpleRouter()
# router = DefaultRouter()

router.register('posts', PostMVS)
router.register('comments', CommentMVS)
router.register('likes', LikeMVS)

post_base_router = NestedSimpleRouter(router, 'posts', lookup='post')
post_base_router.register('comments', CommentMVS, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(post_base_router.urls)),

]