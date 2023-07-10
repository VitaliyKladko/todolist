from typing import Any

from rest_framework import serializers
# validate_password валидирует пароль по валидаторам, которые указаны в AUTH_PASSWORD_VALIDATORS в settings.py
from django.contrib.auth.password_validation import validate_password


class PasswordField(serializers.CharField):
    def __int__(self, **kwargs: Any) -> None:
        kwargs['style'] = {'input_type': 'password'}
        kwargs.setdefault('write_only', True)
        kwargs.setdefault('required', True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)
