from django import forms

class VideoForm(forms.Form):
    videoName = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'id': 'inputName'
        }))
    videoDescription = forms.CharField(widget=forms.Textarea(attrs = {
        'class': 'form-control',
        'rows': '5',
        'id': 'comment',
        'placeholder': 'Comment'
    }))