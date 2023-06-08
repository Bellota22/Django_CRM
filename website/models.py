from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #adding timestamp
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name} ")