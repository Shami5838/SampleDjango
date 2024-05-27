from django.db import models

# Create your models here.
class bioData(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    father_name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)

    def __str__(self):
        return self.name
