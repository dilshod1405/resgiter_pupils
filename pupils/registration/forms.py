from django import forms

from .models import Pupil, Region, School_location


class PupilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class_number = forms.IntegerField()
    birth_date = forms.DateField()

    class Meta:
        model = Pupil
        fields = '__all__'
