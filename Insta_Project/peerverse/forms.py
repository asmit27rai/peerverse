from django import forms
from .models import Post,UserMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'photo', 'file', 'is_important']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and not user.is_superuser:
            self.fields['is_important'].disabled = True

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), label="To (Username)")

    class Meta:
        model = UserMessage
        fields = ['receiver', 'subject', 'message']