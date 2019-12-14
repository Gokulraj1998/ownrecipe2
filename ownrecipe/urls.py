from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.page1 ),
    path('signupdone', views.signup),
    
    ]
