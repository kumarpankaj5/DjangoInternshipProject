# consumer_services/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('submit/', views.submit_service_request, name='submit_service_request'),    
    path('tracking/', views.request_tracking, name='request_tracking'),
     path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
# urls.py


