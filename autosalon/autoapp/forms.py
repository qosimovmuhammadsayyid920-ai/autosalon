from django import forms
from .models import Car, Brand

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
            'desctiption': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5,
            })
        }

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