from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>.+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='token'),
    path('v1/', include(router.urls)),
]
