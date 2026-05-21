from django.urls import path
from . import views

app_name = 'resume_builder'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('builder/new/', views.builder, name='new_builder'),
    path('builder/<int:resume_id>/', views.builder, name='builder'),
    path('delete/<int:resume_id>/', views.delete_resume, name='delete_resume'),
]
