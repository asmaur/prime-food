from django.core.exceptions import ValidationError
import re


def zip_code_validator(value):
    # 5-3 /12345-123 ou 12345123
    value = re.sub(pattern="\D", repl="", string=value)
    if len(value) == 8:
        return True
    raise ValidationError(
            "%(value)s não é um número de CEP válido.",
            params={"value": value}
        )
