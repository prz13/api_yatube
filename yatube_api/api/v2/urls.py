from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('posts/<int:post_id>/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
