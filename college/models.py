from django.db import models

class list(models.Model) :
    name = models.CharField(max_length=200 , unique=True)
    rank = models.IntegerField()
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class details(models.Model) :
    name = models.ForeignKey(list , on_delete=models.DO_NOTHING)
    year_of_stablishment = models.IntegerField()
    mode_of_admission = models.CharField(max_length=300)
    def __str__(self):
        return self.name
