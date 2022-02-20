from django_filters import rest_framework

from .models import Title


class TitleFilter(rest_framework.FilterSet):
    name = rest_framework.filters.CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    category = rest_framework.filters.CharFilter(
        field_name='category__slug',
    )
    genre = rest_framework.filters.CharFilter(
        field_name='genre__slug',
    )

    class Meta:
        model = Title
        fields = (
            'name',
            'year',
            'category',
            'genre',
        )
