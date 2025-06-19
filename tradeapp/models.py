from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    confirm_password = models.CharField(max_length=128, blank=True, null=True)
    key = models.CharField(max_length=128, blank=True, null=True)
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
