from django.urls import path
from .import views

urlpatterns = [
    path('',views.log),
    path('register',views.reg ,name='register'),
    path('lout',views.lout, name='lout'),
    path('admdash',views.admdash),
    path('add/',views.addp, name='add'),
    path('edit/<str:pid>/', views.editp),
    path('dele/<pid>',views.delp, name='dele'),
    path('upb/',views.update_banner, name='upb'),
    path('addcat/',views.add_cat, name='addcat'),
    path('delecat/<int:cat_id>/',views.dele_cat, name='delecat'),
    path('viewproduct', views.viewp),
    path('u_home',views.uhome, name='u-home'),
    path('addw', views.addws, name='add_weight'),
    path('editweight/<str:pid>/', views.editws, name='edit_weight'),
    path('products/<category_id>', views.product_list), 
    path('search/', views.search_products, name='search_products'),
    path('singlep/<pid>', views.single_product)
]
