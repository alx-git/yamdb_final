from django.contrib import admin

from .models import Category, Genre, Title


class CategoryGenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'description',
    )
    search_fields = (
        'name',
        'slug',
    )
    list_filter = (
        'name',
        'slug',
    )
    list_editable = ('slug',)
    empty_value_display = '--empty--'


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'category',
        'genre_display',
    )
    search_fields = (
        'name',
        'year',
        'category',
    )
    list_filter = (
        'name',
        'year',
        'category',
    )
    list_editable = ('year', 'category',)
    empty_value_display = '--empty--'

    def genre_display(self, object):
        return object.genre

    genre_display.empty_value_display = '--empty--'


admin.site.register(Category, CategoryGenreAdmin)
admin.site.register(Genre, CategoryGenreAdmin)
admin.site.register(Title, TitleAdmin)
