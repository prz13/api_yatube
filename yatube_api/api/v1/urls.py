from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')

comment_router = DefaultRouter()
comment_router.register(r'', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', 
         include(comment_router.urls), 
         name='comment-list'),
]

