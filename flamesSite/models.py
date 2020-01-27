from django.db import models

# Create your models here.

class name(models.Model):
    first_name = models.CharField(max_length=2000)
    second_name = models.CharField(max_length=2000)

    def __str__(self):
        return self.first_name+" "+self.second_name
