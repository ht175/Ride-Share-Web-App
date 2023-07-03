from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

def UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        Model= NormalUser
        fields = ("username", "email", "password1", "password2")

def UserLoginForm(forms.form):
    username = forms.CharField(max_length=16)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "),
        'inactive': _("This account is not registered, please register first."),
    }

def RideCreationForm(forms.ModelForm): #ModelForm has save method
    class Meta:
        Model = Ride
        fields = ("ride_type","owner_passenger_num","destination","arrive_time","special_requeest","vehicle_type")
    # clean data : make sure passenger_num cannot less than 1
    def clean_passenger_num(self):
        num = self.cleaned_data['owner_passenger_num']
        if num<1 :
             raise ValidationError('Invalid passenger number')
        return num

    # clean data: make sure arrive_time not earlier than now
    def clean_arrive_time(self):
        time =self.cleaned_data["arrive_time"]
        if time<timezone.now() :
            raise ValidationError('Invalid arrive time ')
        return time


def DriverCreationForm(forms.ModelForm):
    class Meta:
        Model = Driver
        fields =("vehicle_type","max_num","plate_number","special_info")



def ShareCreateForm(forms.Form):
    destination = models.CharField(MAXIMUM_NUM=256)
    earliest_time = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD HH-MM</em>.")
    latest_time = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD HH-MM</em>.")
    passenger_num = models.IntegerField()
    #  clean data : make sure passenger_num cannot less than 1
    def clean_passenger_num(self):
        num = self.cleaned_data['passenger_num']
        if num<1 :
             raise ValidationError('Invalid passenger number')
        return num
    def clean_arrive_time(self):
        earliest = self.cleaned_data["earliest_time"]
        latest = self.cleaned_data["latest_time"]
        if earliest<timezone.now() :
            raise ValidationError('Invalid arrive time ')
        if latest<timezone.now() :
            raise ValidationError('Invalid arrive time ')
        if earliest>latest:
            raise ValidationError('Invalid arrive time ')
        return earliest,latest
        
     