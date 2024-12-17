from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    # Define choices for categorical fields
    PCLASS_CHOICES = [(1, "First Class"), (2, "Second Class"), (3, "Third Class")]
    SEX_CHOICES = [(1, "Male"), (0, "Female")]
    EMBARKED_Q_CHOICES = [(1, "Yes"), (0, "No")]
    EMBARKED_S_CHOICES = [(1, "Yes"), (0, "No")]

    Pclass = forms.ChoiceField(choices=PCLASS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Sex_male = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Embarked_Q = forms.ChoiceField(choices=EMBARKED_Q_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Embarked_S = forms.ChoiceField(choices=EMBARKED_S_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Passenger
        fields = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_male', 'Embarked_Q', 'Embarked_S']
        widgets = {
            'Age': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'SibSp': forms.NumberInput(attrs={'class': 'form-control'}),
            'Parch': forms.NumberInput(attrs={'class': 'form-control'}),
            'Fare': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }
