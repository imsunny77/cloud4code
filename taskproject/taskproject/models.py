from django.db import models
import uuid
from .choices import *

class BaseModel(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position    = models.PositiveSmallIntegerField("Position", null=True, blank=True)
    display_status = models.IntegerField("Status", choices=DisplayStatus.choices, default=DisplayStatus.PUBLISH)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True