from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='photos')
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of {self.user.first_name}"