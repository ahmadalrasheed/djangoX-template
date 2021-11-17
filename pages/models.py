from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Snack(models.Model):
    """
    This class is declaring the model of the data (thier shape) that we want to add into database
    """

    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE )
    snack = models.IntegerField(default=0)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snackdetails' , args=[str(self.pk)])



