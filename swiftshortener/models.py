from django.db import models

# Create your models here.
class URL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.long_url