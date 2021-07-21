from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    class Meta:
        db_table = "owners"

    

