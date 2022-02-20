from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    roles = (
        ('admin', 'admin'),
        ('moderator', 'moderator'),
        ('user', 'user'),
    )

    email = models.EmailField(unique=True)
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=20,
        choices=roles,
        default='user',
    )

    class Meta:
        ordering = ['id']

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'
