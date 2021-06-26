"""electionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup', views.votersignup, name='signup'),
    path('login', views.voterlogin, name='login'),
    path('logout', views.voterlogout, name='logout'),
    path('signend', views.signend, name='signend'),
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name="voter_account/resetpassword.html"), name="reset_password"),
    path('resetpassword_sent/', auth_views.PasswordResetDoneView.as_view(template_name="voter_account/resetdone.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="voter_account/resetconfirm.html"), name="password_reset_confirm"),
    path('resetpassword_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="voter_account/resetcomplete.html"), name="password_reset_complete"),

]
