from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.cow_list, name='cow_list'),
    path('cow/<int:pk>/', views.cow_detail, name='cow_detail'),
    path('cow/new/', views.cow_new, name='cow_new'),
    path('cow/<int:pk>/edit/', views.cow_edit, name='cow_edit'),
    path('cow/<int:pk>/delete/', views.cow_delete, name='cow_delete'),
     path('cow/<int:cow_id>/add_milk_record/', views.add_milk_record, name='add_milk_record'),
    path('login/', auth_views.LoginView.as_view(template_name='cows/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
