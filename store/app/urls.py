from django.urls import path
from .import views

urlpatterns = [
    path('',views.log),
    path('register',views.reg),
    path('lout',views.logout),
    path('admdash',views.admdash),
]
