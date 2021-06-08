from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profileImg = models.ImageField(upload_to='profileImg',blank=True)
    nickName= models.CharField(max_length=20, blank=True)
    intro=models.TextField(blank=True)

# Create your models here.
