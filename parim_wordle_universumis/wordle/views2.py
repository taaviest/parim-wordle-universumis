from django import forms
from django.core.exceptions import ValidationError


def validate_letter(value):
    # Replace ['a', 'b', 'c'] with the list of right letters
    if value.lower() not in ['a', 'b', 'c']:
        raise ValidationError('Wrong letter')