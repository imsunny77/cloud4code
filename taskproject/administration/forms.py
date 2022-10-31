from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

class DateInput(forms.DateInput):
    input_type = 'date'

SEX = (
    (0,'MALE'),
    (1,'FEMALE'),
    (2,'OTHER'),        
)    

class SignUpForm(UserCreationForm):

    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())

    class Meta:
        model = RootUser
        fields = ['email', 'first_name', 'last_name','about','date_of_birth','sex',]

        widgets = {
            'date_of_birth': DateInput(),
            'about': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if not self.instance.email:
            if RootUser.objects.filter(email=data).count() > 0:
                raise forms.ValidationError("User with this email already exists.")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sex', css_class='form-group col-md-2 mb-0'),
                Column('about', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

class RootUserForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())

    class Meta:
        model = RootUser
        fields = ['email', 'first_name', 'last_name','about','date_of_birth','sex',]

        widgets = {
            'date_of_birth': DateInput(),
            'about': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if self.instance.email != data:
            if RootUser.objects.filter(email=data).count() > 0:
                raise forms.ValidationError("User with this email already exists.")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('sex', css_class='form-group col-md-2 mb-0'),
                Column('about', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
        )