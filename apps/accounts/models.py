from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        USER = 'USER', 'Użytkownik'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
        verbose_name="Rola"
    )
    department = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Dział"
    )

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser