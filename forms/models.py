from django.db import models
from multiselectfield import MultiSelectField

class User(models.Model) :
    Name = models.CharField(max_length=100)
    RollNo= models.IntegerField()
    ContactNo = models.IntegerField()
    Email = models.EmailField(max_length=200,unique=True)
    Event = MultiSelectField(choices=(('a','Aptech Rumble'),('b','Games of Codes')))
