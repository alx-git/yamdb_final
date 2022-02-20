from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.permissions import IsAdminOrSuper, IsAuthor, IsModerator, ReadOnly
from .models import Review, Title
from .serializers import (
    CommentSerializer,
    ReviewSerializer,
)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        ReadOnly | IsAuthor | IsModerator | IsAdminOrSuper,
    )
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        if Review.objects.filter(
            title=title,
            author=self.request.user
        ).exists():
            raise ValidationError
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        ReadOnly | IsAuthor | IsModerator | IsAdminOrSuper,
    )
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = get_object_or_404(
            title.reviews.all(),
            pk=self.kwargs.get('review_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        review = get_object_or_404(
            title.reviews.all(),
            pk=self.kwargs.get('review_id')
        )
        serializer.save(
            author=self.request.user,
            review=review
        )
