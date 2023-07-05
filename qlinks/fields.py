from django.core.validators import RegexValidator
from django.db import models
from django.forms import SlugField

URL_SLUG_VALIDATOR = RegexValidator(r'^[-a-zA-Z0-9_/]+\Z')


class ShortURLFormField(SlugField):
    default_validators = [URL_SLUG_VALIDATOR]


class ShortURLField(models.SlugField):
    default_validators = [URL_SLUG_VALIDATOR]

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': ShortURLFormField,
            **kwargs,
        })
