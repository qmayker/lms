import re

from django.core.validators import RegexValidator


class UsernameValidator(RegexValidator):
    regex = re.compile(pattern=r"[^A-Za-z0-9_]")
    inverse_match = True
    message = "Username can contain only letters, numbers and _"
