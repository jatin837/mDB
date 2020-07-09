from django import forms

class NameForm(forms.Form):
    user_name = forms.CharField(label = 'enter you name', max_length = 12)
