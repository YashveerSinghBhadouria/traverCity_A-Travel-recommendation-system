from django import forms
from django.contrib.auth.models import User
from travel_app.models import Usersignup  , Questionnaire

GENDER_CHOICES = [
   ('Male', 'Male'),
   ('Female', 'Female')
]

MARITAL_CHOICES = [
    ('Single', 'Single'),
    ('Married', 'Married')
]

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,6)]

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Username') #, widget=forms.TextInput(attrs={'class' : 'special'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class' : 'myemailclass'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UsersignupForm(forms.ModelForm):

    gender= forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    marital_status= forms.ChoiceField(choices=MARITAL_CHOICES, widget=forms.RadioSelect())
    #DOM=forms.DateField(input_formats=['%d/%m/%y'])

    class Meta():
        model = Usersignup
        fields = ('name','contact_no','dob','gender','marital_status')
        # widgets = {'gender': forms.RadioSelect(choices=[('M', 'Male'),('F', 'Female')]),'marital_status':forms.RadioSelect(choices=[('S', 'Single'),('M', 'Married')]), 'password': forms.PasswordInput()}
        # preferred_drink = forms.ChoiceField(choices=PREFERRED_DRINK_CHOICES,
        #                                 widget=forms.RadioSelect())

class QuestionnaireForm(forms.ModelForm):

    adventure = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    heritage = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    wildlife = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    nature = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    pilgrimage = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    couple = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    friends = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    family = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    winter = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    spring = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    summer = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    monsoon = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    autumn = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    young = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    mid_age = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    old = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    #visited_state = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    #visited_city = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    rate_place = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    #budget = forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))

    class Meta():
        model = Questionnaire
        fields = ('username','adventure','heritage','wildlife','nature','pilgrimage','couple','friends','family','winter','spring','summer','monsoon','autumn','young','mid_age','old','visited_state','visited_city','rate_place','budget')
