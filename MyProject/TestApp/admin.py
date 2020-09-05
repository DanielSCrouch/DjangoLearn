from django.contrib import admin
from .models import App, App2, RegistrationData

# Register your models here.


admin.site.register(App) 
admin.site.register(App2)
admin.site.register(RegistrationData)