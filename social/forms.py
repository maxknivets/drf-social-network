from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from social.models import Post

class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField()

class PostForm(forms.Form):
    post_text = forms.CharField(min_length=1, max_length=2500, widget=forms.TextInput(attrs={'placeholder': 'How was your day?', 'id': 'post-field'}))
    post_image = forms.ImageField(required=False)

class EditForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'edit-id'}))
    new_text = forms.CharField(min_length=1, max_length=2500, widget=forms.TextInput(attrs={'placeholder': 'Edit here', 'id': 'edit-field'}))

class DeleteForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'delete-id'}))

class CommentForm(forms.Form):
    comment = forms.CharField(min_length=1, max_length=2500, widget=forms.TextInput(attrs={'placeholder': 'What do you think?', 'id': 'comment-field'}))
    id = forms.IntegerField(widget=forms.HiddenInput())
    in_reply_to_user = forms.IntegerField(widget=forms.HiddenInput())
    in_reply_to_comment = forms.IntegerField(widget=forms.HiddenInput())

class ChangeForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Your first name', 'id': 'first-name-field'}))
    last_name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Your last name', 'id': 'last-name-field'}))
    bio = forms.CharField(max_length=2500, required=False, widget=forms.TextInput(attrs={'placeholder': 'Tell something cool', 'id': 'bio-field'}))
    location = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Your current location', 'id': 'location-field'}))

class PFPForm(forms.Form):
    profile_picture = forms.ImageField()
    

