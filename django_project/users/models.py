from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель пользователей системы"""

    phone = models.CharField(
        unique=True,
        max_length=50,
    )
    tg_id = models.IntegerField(unique=True)
