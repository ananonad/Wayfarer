from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Planet(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_planet = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()

#     def __str__(self):
#         return self.user.username
#class User(AbstractUser):