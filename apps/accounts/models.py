from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser to support
    role-based access control (RBAC) across the ELRS system.
    """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        IT_MANAGER = 'IT_MANAGER', 'IT Manager'
        EMPLOYEE = 'EMPLOYEE', 'Employee'

    role = models.CharField(
        max_length=15,
        choices=Role.choices,
        default=Role.EMPLOYEE,
        verbose_name="System role"
    )

    @property
    def is_admin(self):
        """Check if the user has full Administrator privileges."""
        return self.role == self.Role.ADMIN or self.is_superuser
    
    @property
    def is_it_manager(self):
        """Check if the user has IT Manager or higher privileges."""
        return self.role in (self.Role.ADMIN, self.Role.IT_MANAGER) or self.is_superuser

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"