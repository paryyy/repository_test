from django.db import models

# Create your models here.
class jam_majzur(models.Model):
    first_number=models.DecimalField(max_digits=10, decimal_places=4)
    second_number=models.DecimalField(max_digits=10, decimal_places=4)
