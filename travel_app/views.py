from django.shortcuts import render
from travel_app.forms import UserForm,UsersignupForm, QuestionnaireForm
from travel_app.models import Usersignup  ,Questionnaire
from travel_app.GettingStarted import Get
#from datarel import datarel

###
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required  #****
from django.contrib.auth.backends import ModelBackend, UserModel

# Create your views here.
def index(request):
    return render(request, 'travel_app/index.html')

def newq(request):
    return render(request, 'travel_app/newq.html')

def destination(request):
    Getting_Started = Get()
    # console.log(Getting_Started.recommendations)
    print("sfsdf")
    print(Getting_Started[0])
    gs0 = Getting_Started[1]
    gs1 = Getting_Started[2]
    gs2 = Getting_Started[3]
    gs3 = Getting_Started[4]
    gs4 = Getting_Started[5]
    gs5 = Getting_Started[6]
    gs6 = Getting_Started[7]
    return render(request, 'travel_app/destination.html',{'gs0':gs0,'gs1':gs1,'gs2':gs2,'gs3':gs3,'gs4':gs4,'gs5':gs5,'gs6':gs6})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):

    registered = False
    #username = None
    if request.method == 'POST':

        # userregister=Userregistration()
        # userregister.name = request.POST.get('name')
        # userregister.email = request.POST.get('email')
        # userregister.username = request.POST.get('username')
        # userregister.password = request.POST.get('password')
        # userregister.contact_no = request.POST.get('phone')
        # userregister.dob = request.POST.get('birthday')
        # userregister.gender = request.POST.get('gender')
        # userregister.marital_status = request.POST.get('status')
        #userregister.dom = request.POST.get('anniversary')
        #print(userregister.Gender)

        user_form = UserForm(data=request.POST)
        usersignup_form = UsersignupForm(data=request.POST)

        if user_form.is_valid() and usersignup_form.is_valid():
            # username = request.POST.get('username')
            # print(username)
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            usersignup = usersignup_form.save(commit=False)
            usersignup.user = user
            usersignup.save()
        # userregister.set_password(user.set_password)
        # userregister.save()

            registered = True

        else:
            print(user_form.errors, usersignup_form.errors)


    else:
        user_form = UserForm()
        usersignup_form = UsersignupForm()
        # userregister = UserregistrationForm()
    return render(request,'travel_app/signup.html',
                            {'user_form':user_form,
                             'usersignup_form':usersignup_form,
                             #'username': username,
                              'registered':registered})


def user_login(request):

      if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = authenticate(username=username, password=password)
          print(user)
          if user is not None:
              print("Hey")
              if user.is_active:
                  print("Hello")
                  login(request,user)
                  return HttpResponseRedirect(reverse('user_home'))
              else:
                  print("else first")
                  return HttpResponse("ACCOUNT NOT ACTIVE")

          else:
              print("Someone tried to login and failed!")
              print("username: {} and password: {} ".format(username,password))
              return HttpResponse("invalid login details supplied")
      else:
          return render(request,'travel_app/user_login.html',{})

def newq(request):

    filled = False

    # username = request.get('username')
    #print(username)
    if request.method == 'POST':

        ques = QuestionnaireForm(request.POST)
        #username = post.objects.get(username=username)
        #print(username)
        if ques.is_valid():

            instance = ques.save(commit=False)
            instance.username = request.user
            instance.save
            ques.adventure = request.POST.get('adventure')
            ques.heritage = request.POST.get('heritage')
            ques.wildlife = request.POST.get('wildlife')
            ques.nature = request.POST.get('nature')
            ques.pilgrimage = request.POST.get('pilgrimage')
            ques.couple = request.POST.get('couple')
            ques.friends = request.POST.get('friends')
            ques.family = request.POST.get('family')
            ques.winter = request.POST.get('winter')
            ques.spring = request.POST.get('spring')
            ques.summer = request.POST.get('summer')
            ques.monsoon = request.POST.get('monsoon')
            ques.autumn = request.POST.get('autumn')
            ques.young = request.POST.get('young')
            ques.mid_age = request.POST.get('midage')
            ques.old = request.POST.get('old')
            ques.visited_state = request.POST.get('stt')
            ques.visited_city = request.POST.get('city')
            ques.rate_place = request.POST.get('place')
            ques.budget = request.POST.get('budget')

        else:
            print(ques.errors)

        filled = True

    else:
        ques = QuestionnaireForm()

    return render(request,'travel_app/newq.html',
                    {'filled':filled})


# class EmailBackend(ModelBackend):  # pylint: disable=too-few-public-methods
#     '''
#     Authentication backend class which authenticates the user against his
#     e-mail address instead of his username.
#     '''
#
#     def authenticate(self, username=None, password=None, **kwargs):  # pylint: disable=unused-argument
#         '''
#         Authenticate the user via his e-mail address.
#
#         :param str username: The username used to authenticate
#         :param str password: The password used to authenticate
#         :return: When successful, the User model is returned
#         :rtype: User model or None
#         '''
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
#
#         return None
