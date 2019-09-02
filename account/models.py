from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nnp_user = models.CharField(max_length=120)
    nnp_pass = models.CharField(max_length=120)

    def __str__(self):
        return user.firstname