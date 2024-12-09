from django.urls import path
from .import views

urlpatterns = [
    path('',views.log),
    path('register',views.reg),
    path('lout',views.lout),
    path('admdash',views.admdash),
    path('add/',views.addp),
    path('edit/',views.editp),
    path('dele/',views.delp),
]
