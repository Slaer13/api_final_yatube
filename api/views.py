from rest_framework import filters
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Group, User

from .permissions import IsAuthorOrReadOnly
from .serializers import (PostSerializer, CommentSerializer, FollowSerializer,
                          GroupSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BaseCreateListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    pass


class FollowViewSet(BaseCreateListViewSet):
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']
    filterset_fields = ['user']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.following.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(BaseCreateListViewSet):
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        return Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
        return post.comments.all()
