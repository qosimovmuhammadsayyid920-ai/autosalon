from django import forms
from .models import Car, Brand
from django.core.validators import ValidationError

class BrandForm(forms.ModelForm):
    class Meta: 
        model = Brand
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'founded_year': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5,
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if not name.isalpha():
            raise ValidationError("Nomi faqat harflarda bolishi kerak!!!!")
        
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 50:
            raise ValidationError('Haqidagi malumot 50 ta harfadan iborat bolsin!!!')
        return description
            

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'dvigitel': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'probeg': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_avaible': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        year = cleaned_data.get('year')
        if len(str(year)) != 4:
            raise ValidationError('Yili 4 ta sondan iborat bolishi kerak!!!')
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if len(str(price)) >= 10:
            raise ValidationError('Narxi 10 ta sonlardan iborat bolishi kerak!!!')
        return price
    
class CommentForm(forms.Form):
    text = forms.CharField(max_length=100)
    
