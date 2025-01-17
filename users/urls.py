from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # login page
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
    # logging out page
    path('logging_out/', views.logging_out, name='logging_out'),
]