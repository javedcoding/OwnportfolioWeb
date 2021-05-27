from django.db import models

# Create your models here.


class TextLevel(models.Model):
    title = models.CharField(max_length=50)
    words = models.TextField(max_length=1200)
    date = models.DateField()

    def __str__(self):
        return self.title
