from django.contrib import admin
from django.urls import path,include
from emailSend import views
urlpatterns = [
     path('',views.index, name='index'),
    path('mail',views.send,name='mail')
] 
