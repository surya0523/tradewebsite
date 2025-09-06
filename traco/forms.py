from django import forms
from django.contrib.auth.models import User

CITY_CHOICES = [
    ('', 'Select your city'),  
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Bangalore', 'Bangalore'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
]

# Partner Form
class PartnerForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-input w-full px-4 py-2 rounded-lg'}))
    phone = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input w-full px-4 py-2 rounded-lg'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-Mail Id', 'class': 'form-input w-full px-4 py-2 rounded-lg'}))
    pincode = forms.CharField(max_length=6, min_length=6, widget=forms.TextInput(attrs={'placeholder': 'Pin Code', 'class': 'form-input w-full px-4 py-2 rounded-lg'}))
    city = forms.ChoiceField(choices=CITY_CHOICES,  widget=forms.Select(attrs={'class': 'form-input w-full px-4 py-2 rounded-lg'}))

# Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'E-mail Id', 'class': 'form-input w-full px-4 py-2 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-input w-full px-4 py-2 rounded-xl'}))


class RegisterForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=10, min_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input w-full px-4 py-2 rounded-xl'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-input w-full px-4 py-2 rounded-xl'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-input w-full px-4 py-2 rounded-xl'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'E-mail Address',
                'class': 'form-input w-full px-4 py-2 rounded-xl'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-input w-full px-4 py-2 rounded-xl'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    
# ✅ Verify OTP Form
class VerifyOtpForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter OTP',
            'class': 'form-input w-full px-4 py-2 rounded-xl'
        })
    )