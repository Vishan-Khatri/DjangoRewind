from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    college = models.CharField(max_length=200)
    phone   = models.CharField(max_length=15, blank=True)
    city    = models.CharField(max_length=100, default='Kathmandu')
    bio     = models.TextField(blank=True, max_length=300)

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.college}"
