"""
URL configuration for employee_tracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from employee_tracking.employees.views import admin_dashboard, approve_leave, reject_leave

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve_leave/<int:leave_id>/', approve_leave, name='approve_leave'),
    path('reject_leave/<int:leave_id>/', reject_leave, name='reject_leave'),
]
