from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    banner = models.ImageField(upload_to='theme/')
    main_caption = models.CharField(max_length=150)
    sub_caption = models.TextField(max_length=200)