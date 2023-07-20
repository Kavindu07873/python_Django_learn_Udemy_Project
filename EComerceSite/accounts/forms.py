from django import forms 
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    Confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))

    # methana normal user kenekta ona dewal witharai add karnne
    # me meta data tika mulinma balanawa normal userge dewalda kiyala 
    class Meta:
        model = Account
        fields = ['first_name','last_name','email','password','phone_number']
        # fields = ['first_name','last_name','email','password']


    # apita loop ekak through serama atribute walata css add karanna puluwan
    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter_first_name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter_last_name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter_email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter_phone_number'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
