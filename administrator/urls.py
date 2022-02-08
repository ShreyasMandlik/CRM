from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('administrator_login',views.administrator_login, name='administrator_login'),
    path('logout',views.logout_view, name='logout'),
    path('administrator_home',views.administrator_home, name='administrator_home'),
    path('Agent_Signup',views.Agent_Signup, name='Agent_Signup'),
    path('administrator_Signup',views.administrator_Signup, name='administrator_Signup'),
    path('service_add',views.service_add, name='service_add'),
    path('service_update/<str:pk>',views.service_update, name='service_update'),
    path('service_delete/<str:pk>',views.service_delete, name='service_delete'),
    path('approve_trial/<str:pk>',views.approve_trial, name='approve_trial'),
    path('Delete_trial/<str:pk>',views.Delete_trial, name='Delete_trial'),
]