from django.conf.urls import url
from travel_app import views

#TEMPLATE URLS
app_name = 'travel_app'

urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^newq/$', views.newq, name='newq'),
    url(r'^destination/$',views.destination,name='destination'),
#r'^users/(?P<user_id>\d+)/$'
]
