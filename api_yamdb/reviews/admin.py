from django.contrib import admin

from .models import Comment, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'author',
        'pub_date',
        'score',
    )
    search_fields = (
        'title',
        'author',
        'pub_date',
        'score',
    )
    list_filter = (
        'title',
        'author',
        'score',
    )
    list_editable = ('score',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'review',
        'pub_date',
    )
    list_filter = (
        'author',
        'pub_date',
    )
    search_fields = (
        'author',
        'pub_date',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
