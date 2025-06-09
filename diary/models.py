
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class PhotoEntry(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='photos/')
    caption=models.CharField(max_length=255)
    date_uploaded=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.caption}-{self.date_uploaded}"
    class Meta:
        verbose_name="PhotoEntry"
        verbose_name_plural="PhotoEntry"