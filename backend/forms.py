from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from backend.models import Post

class Sign_up_form(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(Sign_up_form, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2',]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')