from django.urls import path
from .import views

urlpatterns = [
    path('',views.log),
    path('register',views.reg),
    path('lout',views.lout, name='lout'),
    path('admdash',views.admdash),
    path('add/',views.addp, name='add'),
    path('edit/',views.editp, name='edit'),
    path('dele/',views.delp, name='dele'),
    path('upb/',views.update_banner, name='upb'),
    path('addcat/',views.add_cat, name='addcat'),
    path('delecat/<int:cat_id>/',views.dele_cat, name='delecat'),
]
