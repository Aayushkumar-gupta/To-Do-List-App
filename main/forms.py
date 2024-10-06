from django import forms


# Form to Create a new to-do-list
class CreateNewList(forms.Form):
    name = forms.CharField(max_length=200)      # Collects the name of to-do-list
    #check = forms.BooleanField(required = False)        # Doesn't really needed and add additional functionality