from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='')
    image = models.ImageField(upload_to='series/')

    def __str__(self):
        return f'{self.title}'
