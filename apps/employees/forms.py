from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Form for creating and updating employee records."""

    class Meta:
        model = Employee

        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "position",
            "department",
            "employment_date",
            "is_active",
            "user",
        ]

        widgets = {
            "employment_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
