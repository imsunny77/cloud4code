from django.db import models

class DisplayStatus(models.IntegerChoices):
    PUBLISH = 0, ('PUBLISH')
    DRAFT   = 1, ('DRAFT')

    __empty__ = ('SELECT')