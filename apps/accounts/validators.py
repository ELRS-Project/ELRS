import re
from django.core.exceptions import ValidationError


class CustomPasswordComplexityValidator:
    """
    Validate that the password contains at least one uppercase letter
    and at least one special character.
    """

    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "The password must contain at least one uppercase letter.",
                code='password_no_upper',
            )
        if not re.search(r'[^A-Za-z0-9]', password):
            raise ValidationError(
                "The password must contain at least one special character.",
                code='password_no_special',
            )

    def get_help_text(self):
        return (
            "Your password must contain at least one uppercase letter "
            "and at least one special character."
        )