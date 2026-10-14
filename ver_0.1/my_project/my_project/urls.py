"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('departments/', views.department_list, name='departments'),
    path('employees/', views.employee_list, name='employees'),
    path('task-types/', views.task_type_list, name='task-types'),
    path('task-links/', views.task_link_list, name='task-links'),
    path('tasks/', views.task_list, name='tasks'),
    path('projects/', views.project_list, name='projects'),
    path('project-roles/', views.project_role_list, name='project-roles'),
    path('project-participations/', views.project_participation_list, name='project-participations'),
    path('time-entries/', views.time_entry_list, name='time-entries'),
]





