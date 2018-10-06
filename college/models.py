from django.db import models

class list(models.Model) :
    name = models.CharField(max_length=200 , unique=True)
    rank = models.IntegerField()
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

