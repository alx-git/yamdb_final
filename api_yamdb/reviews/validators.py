from django.core.exceptions import ValidationError


def validatescore(value):
    if not (0 <= value <= 10):
        raise ValidationError(
            f'{value} не является подходящим значением для рейтинга',
            params={'value': value},
        )
