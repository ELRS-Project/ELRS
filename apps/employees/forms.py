from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Form for creating and updating employee records."""

    def __init__(self, *args, **kwargs):
        """Initialize the form and apply Bootstrap styling to its widgets."""

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, forms.CheckboxInput):
                widget.attrs["class"] = "form-check-input"
            elif isinstance(widget, forms.Select):
                widget.attrs["class"] = "form-select"
            else:
                widget.attrs["class"] = "form-control"

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
