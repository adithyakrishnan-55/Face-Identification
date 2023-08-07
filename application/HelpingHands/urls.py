"""HelpingHands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPage),
    path('AdminHome/', AdminHome, name='AdminHome'),
    path('Regestudent/',Regestudent, name='Regestudent'),
    path('SaveStore/',SaveStore, name='SaveStore'),
    path('LoginPage/',LoginPage, name='LoginPage'),
    path('CheckLogin/',CheckLogin, name='CheckLogin'),
    path('Studentlogin/',Studentlogin, name='Studentlogin'),
    path('student_check/',student_check, name='student_check'),
    path('View_employee/',View_employee, name='View_employee'),
    path('GetallUsers/',GetallUsers, name='GetallUsers'),
    path('Updatestudent/',Updatestudent, name='Updatestudent'),
    path('Student_home/',Student_home, name='Student_home'),
    path('Admin_view_attendance/',Admin_view_attendance, name='Admin_view_attendance'),
    path('get_attendance_data/',get_attendance_data, name='get_attendance_data'),
    path('Student_view_attendance/',Student_view_attendance, name='Student_view_attendance'),
    path('student_get_attendance/',student_get_attendance, name='student_get_attendance'),
    path('Admin_view_salary/',Admin_view_salary, name='Admin_view_salary'),
    path('getfaceusid/',getfaceusid, name='getfaceusid'),
    path('Admin_cap_img/',Admin_cap_img, name='Admin_cap_img'),
    path('Getimage/',Getimage, name='Getimage'),
    path('getsaveface/',getsaveface, name='getsaveface'),
    path('Admin_add_subject/',Admin_add_subject, name='Admin_add_subject'),
    path('Save_subject/',Save_subject, name='Save_subject'),






]
