from django.urls import path
from .views import AppView, AppDateView, Home, Contact, register, addUser

urlpatterns = [
    path('', Home, name='Home'),
    path('app/', AppView, name='TestApp'),
    path('appdate/<int:year>', AppDateView, name='TestAppDate'),
    path('contact/', Contact, name='Contact'),
    path('signup/', register, name='register'),
    path('addUser/', addUser, name='addUser')
]

