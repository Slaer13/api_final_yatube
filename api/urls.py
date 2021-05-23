from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet
)

router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('group', GroupViewSet, basename='group')
router.register('posts', PostViewSet, basename='post')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
