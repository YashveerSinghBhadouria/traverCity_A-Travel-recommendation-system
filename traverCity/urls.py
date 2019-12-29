"""traverCity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from travel_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^$',views.newq,name='newq'),
    url(r'^admin/', admin.site.urls),
    url(r'^travel_app/',include('travel_app.urls',namespace="travel_app")),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),

]
