from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
from datetime import timedelta

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email


class OneTimeToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timedelta(minutes=10))

    def is_valid(self):
        return timezone.now() < self.expiration_date