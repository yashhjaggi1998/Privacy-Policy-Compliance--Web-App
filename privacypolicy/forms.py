from django import forms

class InputForm(forms.Form):
	weblink = forms.CharField(max_length=1000 , widget= forms.TextInput( attrs = {'id':'search'} ))