from django.db import models
from django.db.models import Model
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class NormalUser(User):
    is_a_driver = models.BooleanField(default=False)
    def __str__(self):
        return super().get_username()


MAXIMUM_NUM = (
    (1, "1"),
    (4, "4"),
    (6, "6"),
)

SHARE_CHOICE ={
    (True,"share"),
    (False,"not share")
}

TYPE_CHOICE = (
    ('c', 'comfort'),
    ('x', 'luxury'),
)

RIDE_STATUS = (
        ('op', 'open'),
        ('cf', 'confirmed'),
        ('cp', 'complete'),
    )

class Driver(models.Model):
    Driver = models.OneToOneField(NormalUser, on_delete = models.CASCADE) #When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
    vehicle_type = models.CharField(max_length=1,choices=TYPE_CHOICE,default='c')
    max_num = models.IntegerField(choices=MAXIMUM_NUM)
    plate_number = models.CharField(max_length=8,default='')
    special_info = models.CharField(max_length=128,default='',blank=True) #drive can leave this attribute blank
    def __str__(self):
        return self.vehicle_owner+" "+self.plate_number



class Ride(models.Model):
    ride_type = models.BooleanField(choices=SHARE_CHOICE,default=False) #false or true?
    ride_owner = models.ForeignKey(NormalUser, on_delete = models.CASCADE)
    Driver = models.ForeignKey(Driver, on_delete = models.CASCADE)
    owner_passenger_num = models.IntegerField()
    total_passenger_num = models.IntegerField()
    status = models.CharField(max_length=2,choices=RIDE_STATUS,default='op') #three status open/comfirmed/complete
    destination = models.CharField(max_length=256)
    arrive_time = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD HH-MM</em>.")
    vehicle_type = models.CharField(max_length=1,choices=TYPE_CHOICE,default='c')
    special_requeest = models.CharField(max_length=128,default='',blank=True)
    def __str__(self):
        return self.destination + ' '+self.arrive_time+' Driver:'+self.Driver+' owner: '+self.ride_owner

class Share_info(models.Model):
    ride = models.ForeignKey(Ride, on_delete = models.CASCADE)
    sharer =  models.ForeignKey(NormalUser, on_delete = models.CASCADE)
    sharer_passenger_num = models.IntegerField()
    def __str__(self):
        return self.sharer + " " + self.ride


