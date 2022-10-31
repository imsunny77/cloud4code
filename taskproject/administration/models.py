import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from administration.choices import Sex
from taskproject.models import BaseModel

class RootUser(AbstractUser, BaseModel):
    email = models.EmailField('Email', null=True)
    about = models.TextField('About yourself')
    date_of_birth = models.DateField('Date of Birth',null=True)
    sex = models.IntegerField(choices=Sex.choices, null=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        if self.email:
            self.username = self.email
        super(RootUser, self).save(*args, **kwargs)
    