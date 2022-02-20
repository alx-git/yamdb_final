from django.contrib.auth import get_user_model
from django.db import models
from yamdb.models import Title

from .validators import validatescore

User = get_user_model()


class Review(models.Model):
    text = models.TextField('Текст отзыва')
    score = models.PositiveSmallIntegerField(
        'Рейтинг',
        validators=(validatescore,)
    )
    pub_date = models.DateTimeField(
        'Дата ревью',
        help_text='Дата ревью',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор ревью',
        help_text='Автор ревью'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        help_text='Произведение'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = (models.UniqueConstraint(
            fields=('title', 'author'),
            name='unique_review'
        ),)

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Автор комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='отзыв',
        help_text='отзыв'
    )
    text = models.TextField('Текст комментария')
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]
