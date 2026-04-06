from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    logo = models.ImageField(upload_to='brand/image/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dvigitel = models.CharField(max_length=100)
    probeg = models.IntegerField()
    image = models.ImageField(upload_to='car/image/')
    is_avaible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"