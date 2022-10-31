from django.db import models

class Sex(models.IntegerChoices):
    MALE = 0, ('MALE')
    FEMALE   = 1, ('FEMALE')
    OTHER   = 2, ('OTHER')
