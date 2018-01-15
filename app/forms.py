from django import forms
from django.forms import TextInput, PasswordInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Userpro


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # country = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )
        # widgets = {
        #     'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'first_name': TextInput(attrs={'class': 'form-control'}),
        #     'last_name': TextInput(attrs={'class': 'form-control'}),
        #     'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        #     'password1': PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': PasswordInput(attrs={'class': 'form-control'}),
        # }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # for field in iter(self.fields):
        #     self.fields[field].widget.attrs.update({
        #         'class': 'form-control'
        #     })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            # 'id': 'uname',
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name',
            # 'id': 'fname',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name',
            # 'id': 'lname',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email',
            # 'id': 'email',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            # 'id': 'pass1',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password Confirmation',
            # 'id': 'pass2',
        })

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # user.country = self.cleaned_data['country']
        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
        # exclude = ()


class UserProForm(forms.ModelForm):
    class Meta:
        model = Userpro
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'dob': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'country': forms.TextInput(attrs={'class':'form-control','placeholder':'counrty'}),
            'qualification':forms.Select(attrs={'class':'form-control'}),
        }


        # class UserProForm(forms.ModelForm):
        #     class Meta:
        #         model = Userpro
        #         fields = '__all__'
        #         widgets = {
        #             'user': forms.TextInput(attrs={'readonly': 'readonly'})
        #         }
