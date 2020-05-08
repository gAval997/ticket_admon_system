from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Administrator(User):
    class Meta:
        proxy = True
        ordering = ('first_name',)
