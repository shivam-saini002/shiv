"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index",views.index ,name="indexx"),
    path("con/",views.Contact,name="contactt"),
    path("tra/",views.trainer,name="trainerr"),
    path("why/",views.why,name="whyy"),
    path("",views.signn,name="sig"),
    path("login/",views.login,name="loginn"),
     path("log/",views.logout,name="logoutt"),
    path("otp/",views.otp, name="otpp"),       #signup
    path("email/",views.Email, name="emaill"),
    path("otp1/",views.otp1, name="otpp1"),#forgot
     path("update/",views.Update, name="upd"),
]

