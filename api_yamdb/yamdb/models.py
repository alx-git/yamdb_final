from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        'Категория произведения',
        help_text='Категория произведения',
        max_length=200
    )
    slug = models.SlugField(
        'Слаг категории',
        help_text='Слаг категории',
        unique=True
    )
    description = models.TextField(
        'Описание',
        help_text='Описание',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):
    name = models.CharField(
        'Название жанра',
        help_text='Название жанра',
        max_length=200
    )
    slug = models.SlugField(
        'Слаг жанра',
        help_text='Слаг жанра',
        unique=True
    )
    description = models.TextField(
        'Описание',
        help_text='Описание',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name[:15]


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        help_text='Название произведения',
        max_length=200
    )
    year = models.IntegerField(
        'Год выпуска произведения',
        help_text='Год выпуска произведения'
    )
    description = models.TextField(
        'Описание',
        help_text='Описание',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='Жанр произведения',
        help_text='Жанр произведения'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        related_name='titles',
        verbose_name='Категория произведения',
        help_text='Категория произведения'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведение'
        ordering = ('id',)

    def __str__(self):
        return self.name[:15]


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='titles'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='genres'
    )

    class Meta:
        constraints = (models.UniqueConstraint(
            name='unique_genretitle',
            fields=('genre', 'title')
        ),)

    def __str__(self):
        return f'{self.genre} {self.title}'
