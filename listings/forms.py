from django import forms
from .models import Listing, ContactMessage

class ListingForm(forms.ModelForm):
    class Meta:
        model   = Listing
        exclude = ['owner', 'is_active', 'created_at']
        widgets = {
            'description':    forms.Textarea(attrs={'rows': 4}),
            'available_from': forms.DateInput(attrs={'type': 'date'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model   = ContactMessage
        fields  = ['message']
        widgets = {'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your message here...'})}

class SearchForm(forms.Form):
    CITY   = [('','All Cities')]+[('Kathmandu','Kathmandu'),('Lalitpur','Lalitpur'),('Bhaktapur','Bhaktapur'),('Pokhara','Pokhara'),('Butwal','Butwal'),('Chitwan','Chitwan'),('Biratnagar','Biratnagar'),('Other','Other')]
    GENDER = [('','Any Gender'),('M','Male Only'),('F','Female Only')]
    RTYPE  = [('','All Types'),('single','Single Room'),('shared','Shared Room'),('flat','Whole Flat'),('pg','PG / Hostel')]

    city      = forms.ChoiceField(choices=CITY,   required=False)
    room_type = forms.ChoiceField(choices=RTYPE,  required=False)
    gender    = forms.ChoiceField(choices=GENDER, required=False)
    rent_min  = forms.IntegerField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder':'Min (NPR)'}))
    rent_max  = forms.IntegerField(required=False, min_value=0, widget=forms.NumberInput(attrs={'placeholder':'Max (NPR)'}))
    furnished = forms.BooleanField(required=False)
    wifi      = forms.BooleanField(required=False)
