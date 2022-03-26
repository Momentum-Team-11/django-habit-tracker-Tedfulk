"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from habit import views as habit_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('registration.backends.default.urls')),
    path('', habit_views.login, name='login'),
    path('habit/', habit_views.home, name='home'),
    path('habit/<int:pk>/', habit_views.habit_detail, name='habit_detail'),
    path('habit/<int:pk>/result_list', habit_views.result_detail, name='result_detail'),
    path('habit/add_habit/', habit_views.add_habit, name='add_habit'),
    path('habit/<int:pk>/edit/', habit_views.edit_habit,
         name='edit_habit'),
    path('habit/<int:pk>/delete/', habit_views.delete_habit,
         name='delete_habit'),
    path('habit/<int:pk>/add_result/',
         habit_views.add_result, name='add_result'),
    path('habit/<int:pk>/edit_result/',
         habit_views.edit_result, name='edit_result'),
    path('habit/<int:result_pk>/delete_result/',
         habit_views.delete_result, name='delete_result'),
]
