from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,  null = True, related_name = "+")
    image = models.ImageField(upload_to = 'images/',null = True, blank = True)
