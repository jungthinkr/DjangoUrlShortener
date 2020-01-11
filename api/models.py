from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.long_url + ' / ' + self.short_url
