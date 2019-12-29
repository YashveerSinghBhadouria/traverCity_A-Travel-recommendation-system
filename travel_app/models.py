from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field import formfields
# from phonenumber_field.phonenumber import PhoneNumber, to_python, validate_region
# from phonenumber_field.validators import validate_international_phonenumber

class Usersignup(models.Model):

    user = models.OneToOneField(User,default=None,on_delete=models.PROTECT)

    #additional
    name = models.CharField(null=False, blank = False, max_length=264)

    #email = models.EmailField(null=False, blank=False, default='null')

    #username = models.CharField(null=False, blank=False, default='uname',max_length=10)

    #password = models.CharField(null=False, blank=False, max_length=50, default='null')

    contact_no = models.IntegerField(null=False, blank=False)

    dob = models.DateField(null=False, blank=False)

    gender = models.CharField(max_length=8)

    marital_status = models.CharField(max_length=8)

    #dom = models.DateField(null=False, blank=False)

    def __str__(self):
         return self.user.username


class Questionnaire(models.Model):

    username = models.ForeignKey(Usersignup, default=None, on_delete=models.CASCADE)
    adventure = models.IntegerField(null=False, default=0)
    heritage = models.IntegerField(null=False, default=0)
    wildlife = models.IntegerField(null=False, default=0)
    nature = models.IntegerField(null=False, default=0)
    pilgrimage = models.IntegerField(null=False, default=0)
    couple = models.IntegerField(null=False, default=0)
    friends = models.IntegerField(null=False, default=0)
    family = models.IntegerField(null=False, default=0)
    winter = models.IntegerField(null=False, default=0)
    spring = models.IntegerField(null=False, default=0)
    summer = models.IntegerField(null=False, default=0)
    monsoon = models.IntegerField(null=False, default=0)
    autumn = models.IntegerField(null=False, default=0)
    young = models.IntegerField(null=False, default=0)
    mid_age = models.IntegerField(null=False, default=0)
    old = models.IntegerField(null=False, default=0)
    visited_state = models.CharField(null=False, default='null',max_length=20)
    visited_city = models.CharField(null=False, default='null',max_length=20)
    rate_place = models.IntegerField(null=False, default=0)
    budget = models.IntegerField(null=False, default=0)

    def __str__(self):
        if self.username==None:
            return "ERROR-CUSTOMER USERNAME IS NULL"
        return self.username

# class Citydatabase(models.Model):
#
#     placeid = models.IntegerField(null=False, default='null')
#     city = models.CharField(null=False, default='null', max_length=20)
#     state = models.CharField(null=False, default='null', max_length=20)
#     type = models.CharField(null=False, default='null',max_length=20)
#
#     def __str__(self):
#         return self.placeid
#
# class Ratingdatabase(models.Model):
#
#     userid = models.IntegerField(null=False, default='null')
#     placeid = models.IntegerField(null=False, default='null')
#     rating = models.IntegerField(null=False, default=0)
#     timestamp = models.DateField(null=False, default='null')
#
#     def __str__(self):
#         return self.userid
