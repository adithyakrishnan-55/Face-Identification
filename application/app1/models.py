from django.db import models

# Create your models here.
class Reg_student(models.Model):
    Emp_name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200, unique=True)
    Phone = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    Job_sec = models.CharField(max_length=200)
    B_sal = models.CharField(max_length=200)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)

class Student_table(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200, unique=True)
    Phone = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    Batch = models.CharField(max_length=200)
    Pemail = models.CharField(max_length=200)
    Username = models.CharField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)

class Attendance_table(models.Model):
    Usernm = models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200,default="")
    Punchin=models.CharField(max_length=200)
    Punchout = models.CharField(max_length=200,default="0")


class Subject_table(models.Model):
    Department = models.CharField(max_length=200)
    Semester=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200)
    Stime = models.CharField(max_length=200,default="0")
    Etime = models.CharField(max_length=200,default="0")


class Notify_table(models.Model):
    Date=models.CharField(max_length=200)
  
# class Leave_table(models.Model):
#     Usernm = models.CharField(max_length=200)
#     Date=models.CharField(max_length=200)
#     Reason=models.CharField(max_length=200)
#     Status = models.CharField(max_length=200,default="Not approved")

# class Complaint_table(models.Model):
#     Usernm = models.CharField(max_length=200)
#     Date=models.CharField(max_length=200)
#     Complaint=models.CharField(max_length=200)
# class Salary_table(models.Model):
#     Usernm = models.CharField(max_length=200)
#     Month=models.CharField(max_length=200)
#     Total_attendance = models.CharField(max_length=200)
#     Worked_hours = models.CharField(max_length=200)
#     Salary=models.CharField(max_length=200)
# class Disease_table(models.Model):
#     Dname = models.CharField(max_length=200)
#     Symptoms = models.CharField(max_length=200, unique=True)
# class Medicine_table(models.Model):
#     StoreId = models.CharField(max_length=200)
#     Medname = models.CharField(max_length=200)
#     Medtype = models.CharField(max_length=200)
#     Dname = models.CharField(max_length=200)
#     Symptoms = models.CharField(max_length=200)
#     MedQty = models.CharField(max_length=200,)
#     MedPrice = models.CharField(max_length=200)
#     Date = models.CharField(max_length=200)
# class Reg_public(models.Model):
#     Name = models.CharField(max_length=200)
#     Email = models.CharField(max_length=200)
#     Phone = models.CharField(max_length=200)
#     Bgroup = models.CharField(max_length=200)
#     Address = models.CharField(max_length=200)
#     Latitude = models.CharField(max_length=200)
#     Longitude = models.CharField(max_length=200)
#     Username = models.CharField(max_length=200)
#     Password = models.CharField(max_length=200)
#     Active = models.CharField(max_length=200,default="0")
# class Cart_table(models.Model):
#     Usid = models.CharField(max_length=200)
#     Stid = models.CharField(max_length=200)
#     Medname = models.CharField(max_length=200)
#     Count = models.CharField(max_length=200)
#     Medprice = models.CharField(max_length=200)
#     Total = models.CharField(max_length=200)
# class Order_table(models.Model):
#     Usid = models.CharField(max_length=200)
#     Stid = models.CharField(max_length=200)
#     Medname = models.CharField(max_length=200)
#     Qty = models.CharField(max_length=200)
#     Medprice = models.CharField(max_length=200)
#     Total = models.CharField(max_length=200)
#     Imgid=models.CharField(max_length=200)
#     Date=models.CharField(max_length=200,default="12/11/2021")
#     Paytype=models.CharField(max_length=200,default="")
#     Apprsts=models.CharField(max_length=200,default="0")
#     Delivert_sts=models.CharField(max_length=200,default="0")

# class Reg_donor(models.Model):
#     Name = models.CharField(max_length=200)
#     Place = models.CharField(max_length=200)
#     Phone = models.CharField(max_length=200)
#     Bgroup = models.CharField(max_length=200)
#     Aadhar = models.CharField(max_length=200)
    
#     Username = models.CharField(max_length=200,unique=True)
#     Password = models.CharField(max_length=200)
    
#     Active = models.CharField(max_length=200,default="0")
# class Donation_table(models.Model):
#     Did = models.CharField(max_length=200)
#     Rid = models.CharField(max_length=200)
#     Dname = models.CharField(max_length=200)
#     Dplace=models.CharField(max_length=200)
#     Rname = models.CharField(max_length=200)
#     Rplc = models.CharField(max_length=200,default="Ernakulam")
#     Bldgrp = models.CharField(max_length=200)
#     Reqsts = models.CharField(max_length=200,default="0")
 