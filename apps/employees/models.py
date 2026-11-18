from django.conf import settings
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employee_profile",
        verbose_name="User account"
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name="First name"
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="Last name"
    )

    email = models.EmailField(
        unique=True,
        blank=True,
        null=True,
        verbose_name="Email address"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Phone number"
    )

    position = models.CharField(
        max_length=100,
        verbose_name="Position"
    )

    department = models.CharField(
        max_length=100,
        verbose_name="Department"
    )

    employment_date = models.DateField(
        verbose_name="Employment date"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Is active?"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation date"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Update date"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["last_name", "first_name"]
