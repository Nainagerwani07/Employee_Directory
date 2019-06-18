"""Employee_dir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from .employee_dir import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	re_path(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path("hello",views.welcome_hi,name="hello"),
    path("employee_data",views.Employee_Data,name="employee_data"),
    path("data_table",views.Emp_data,name="data_table"),
    path("emp_update/<int:id>",views.EmployeeTableUpdate,name="emp_data_update"),
    path("homepage",views.homepage,name="homepage")
]
