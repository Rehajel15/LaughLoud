from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, editable=False)
    username = models.CharField(max_length = 20, editable=False)
    isBanned = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)