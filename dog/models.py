from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey('owner.Owner', on_delete=CASCADE)

    class Meta:
        db_table="dogs"

