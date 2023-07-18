from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import uuid

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    Model for handling users related data
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    full_name = models.CharField(
        max_length=50,
        verbose_name='Full Name'
    )
    username = models.CharField(
        max_length=20,
        verbose_name='Username',
        unique=True
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name='Is Active?',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Is Staff?',
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name='Joined',
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    class Meta:
        db_table = 'users'
        ordering = ['full_name']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.full_name
