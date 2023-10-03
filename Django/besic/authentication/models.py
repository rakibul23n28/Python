from django.db import models

from django.contrib.auth.models import User
import uuid
# Create your models here.

class UserActivation(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.UUIDField(default=uuid.uuid4,editable=False)