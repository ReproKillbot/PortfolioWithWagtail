from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class CloudImages(models.Model):
    image = CloudinaryField('image')
    alt_text = models.CharField(max_length=100, default="This image lacks an alternate text!")
