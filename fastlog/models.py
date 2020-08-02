from django.db import models


class booking(models.Model):
    booker=models.CharField(max_length=100)
    initialPlace=models.CharField(max_length=100)
    endPlace=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    distance=models.CharField(max_length=100)
    objectBooked=models.CharField(max_length=100)

    def __str__(self):
        return self.objectBooked

# Create your models here.
