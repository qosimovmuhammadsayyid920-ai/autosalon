from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_transmission(value):
    if value not in ['mexanik', 'avtomat']:
        raise ValidationError('Faqat mexanik yoki avtomat bolishi kerak!!!')
    
def validate_seats(value):
    if value < 1 or value > 8:
        raise ValidationError('Orndiqlar soni eng kopi 8 tagacha bolishi kerak!!!')

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
    tnasmission = models.CharField(max_length=15, default='mexanik', validators=[validate_transmission])
    seats = models.IntegerField(default= 1, validators=[validate_seats])
    is_avaible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    
class Comment(models.Model):
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}"
    
    def __repr__(self):
        return f"Pk: {self.pk}, {self.text}"