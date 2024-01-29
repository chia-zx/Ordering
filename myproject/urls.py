"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from app import views as main_views
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from additem import views as additem_views
from displayitem import views as displayitem_views
from updateitem import views as updateitem_views
from deleteitem import views as deleteitem_views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),
    re_path(r'^additemform$', additem_views.additemform, name='additem_form'),
    re_path(r'^additemconfirmation$', additem_views.additemconfirmation, 
            name='additem_confirmation'),
    re_path(r'^displayitem$', displayitem_views.display_all_items, name='displayitem'),
    re_path(r'^updateitemform$', updateitem_views.updateitemform, name='updateitem_form'),
    re_path(r'^updateitemconfirmation$', updateitem_views.updateitemconfirmation, 
            name='updateitem_confirmation'),
    re_path(r'^deleteitemform$', deleteitem_views.deleteitem_form, name='deleteitemform'),
    re_path(r'^deleteitemconfirmation$', deleteitem_views.deleteitem_confirmation, name='deleteitem_confirmation'),
    

]
