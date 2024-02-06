from django.contrib import admin

# Register your models here.
# customer/browsemenu/apps.py

from django.apps import AppConfig

class BrowsemenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer.browsemenu'
