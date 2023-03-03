from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostMVS


router = DefaultRouter()

router.register('posts', PostMVS)

urlpatterns = [
    path('', include(router.urls)),

]