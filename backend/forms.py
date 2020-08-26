from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from backend.models import Post

class Sign_up_form(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(Sign_up_form, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class Post_form(forms.Form):
    post_text = forms.CharField(min_length=1, max_length=200, widget=forms.Textarea(attrs={
        'placeholder': 'How was your day?',
        'id': 'post-field',
        'cols': '90',
        'rows': '3',
        'class':'post-input form-control my-3'
    }))
    post_image = forms.ImageField(required=False)
    post_image.widget.attrs.update({'class': 'form-control-file my-3'})

class Edit_form(forms.Form):
    id = forms.IntegerField(widget=forms.Textarea(attrs={'id': 'edit-id'}))
    new_text = forms.CharField(min_length=1, max_length=200, widget=forms.Textarea(attrs={
        'placeholder': 'Edit field',
        'id': 'edit-field'
    }))

class Delete_form(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'delete-id'}))

class Change_profile_info_form(forms.Form):
    first_name = forms.CharField(max_length=100, label='', widget=forms.Textarea(attrs={'rows':'2'}))
    last_name = forms.CharField(max_length=100, label='', widget=forms.Textarea(attrs={'rows':'2'}))
    bio = forms.CharField(max_length=100, label='', required=False, widget=forms.Textarea(attrs={'rows':'2'}))
    location = forms.CharField(max_length=100, label='', required=False, widget=forms.Textarea(attrs={'rows':'2'}))

class Profile_picture_form(forms.Form):
    profile_picture = forms.ImageField()
    profile_picture.widget.attrs.update({'id': 'img-input'})