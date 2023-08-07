from ast import Pass
from os import name, replace
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from datetime import datetime
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import paho.mqtt.client as paho
from datetime import datetime
import cv2
import base64
import random
from cropface import capface
from django.conf import settings
# from django.core.mail import send_mail
from sendmail import send_email
datas=""
# Create your views here.
def AdminHome(request):
    return render(request,'admin/adminhome.html',{})
def Regestudent(request):
    return render(request,'admin/Add_employee.html',{})
def SaveStore(request):
    sname=request.GET.get("fname")
    email=request.GET.get("email")
    phone=request.GET.get("phone")
    addr=request.GET.get("addr")
    batch=request.GET.get("jsec")
    pemail=request.GET.get("sal")
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    print(sname,"\n",email,"\n",phone,"\n",addr,"\n",batch,"\n",pemail,"\n",uname,"\n",pswrd)
    try:
        ob=Student_table(Name=sname,Email=email,Phone=phone,Address=addr,Batch=batch,Pemail=pemail,Username=uname,Password=pswrd)
        ob.save()
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        # print(fname+email+phone+role+state+dist+uname+pswrd+admin+addr)
        data={"status":0}
        return JsonResponse(data,safe=False)
def LoginPage(request):

    now = datetime.now()
    dte=now.strftime("%m/%d/%Y")
    current_time = now.strftime("%H:%M:%S")
    try:
        obc=Notify_table.objects.get(Date=dte)
    except:
        ctimelist=current_time.split(":")
        hr=int(ctimelist[0])
        print("current time==>",hr)
        if(hr>=11):

            oba=Attendance_table.objects.filter(Date=dte)
            attlist=[]
            for k in oba:
                if(k.Punchout!="0"):
                    attlist.append(k.Usernm)
            print(attlist)
            print(current_time)
            ob=Student_table.objects.all()
            maillist=[]
            for i in ob:
                uname=i.Username
                pemail=i.Pemail
                
                if(uname not in attlist):
                    maillist.append(pemail)
            print(maillist)
            if(len(maillist)!=0):
                subject = 'ABC college attendance notification'
                message = "Your student is not attended the class today"+"("+dte+")"
            
                
                send_email( subject, message,maillist )
            obn=Notify_table(Date=dte)
            obn.save()
        else:
            pass
    return render(request,'homepage.html',{})
def CheckLogin(request):
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    
    print(uname,pswrd)
    if(uname=="admin@admin.com" and pswrd=="admin"):
        data={"status":3}
        return JsonResponse(data,safe=False)
    else:
        data={"status":0}
        return JsonResponse(data,safe=False)












def Studentlogin(request):
    return render(request,'student/emplogin.html',{})


def View_employee(request):
    return render(request,'admin/View_employee.html',{})

def GetallUsers(request):
    ob=Student_table.objects.all()
    datalist=[]
    for i in ob:
        data={}
        data["Uid"]=i.id
        data["Fname"]=i.Name
        data["Email"]=i.Email
        data["Phone"]=i.Phone
        data["Address"]=i.Address
        data["Batch"]=i.Batch
        data["Pemail"]=i.Pemail
        data["Username"]=i.Username
        data["Password"]=i.Password

        datalist.append(data)
    print(datalist)
    return JsonResponse(datalist,safe=False)


def Admin_add_subject(request):
    ob=Subject_table.objects.all()
    return render(request,'admin/Add_subject.html',{"data":ob})




def Save_subject(request):
    
    dept=request.GET.get("dept")
    sem=request.GET.get("sem")
    sub=request.GET.get("sub")
    stime=request.GET.get("stime")
    etime=request.GET.get("etime")
    print(dept,sem,sub,stime,etime)
    try:
        ob=Subject_table.objects.get(Department=dept,Semester=sem,Subject=sub)
        data={"msg":"no"}
        return JsonResponse(data,safe=False)
    except Exception as e:
        ob=Subject_table(Department=dept,Semester=sem,Subject=sub,Stime=stime,Etime=etime)
        ob.save()
        data={"msg":"yes"}
        print(e)
        return JsonResponse(data,safe=False)




def Updatestudent(request):
    
    uid=request.GET.get("uid")
    fname=request.GET.get("fname")
    email=request.GET.get("email")
    phone=request.GET.get("phone")
    addr=request.GET.get("addr")
    batch=request.GET.get("jsec")
    pemail=request.GET.get("bsal")
    
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
  
    try:
        ob=Student_table.objects.get(id=int(uid))
        ob.Name=fname
        ob.Email=email
        ob.Phone=phone
        ob.Address=addr
        ob.Batch=batch
        ob.Pemail=pemail
        
        ob.Username=uname
        ob.Password=pswrd

        ob.save()
        data={"info":"yes"}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        data={"info":"no"}
        return JsonResponse(data,safe=False)









def student_check(request):
 
    uname=request.GET.get("uname")
    pswrd=request.GET.get("pswrd")
    try:
        ob=Student_table.objects.get(Username=uname,Password=pswrd)
        request.session["usernm"]=uname
        data={"status":1}
        return JsonResponse(data,safe=False)
    except:
        data={"status":0}
        return JsonResponse(data,safe=False)




def Student_home(request):
    return render(request,'student/Student_home.html',{})














def Admin_view_attendance(request):
    return render(request,'admin/view_attendance.html',{})




def get_attendance_data(request):
    name=""
    mnth=request.GET.get("mnth")
    empnm=request.GET.get("empnm")
    print(mnth+"\n"+empnm)
    mnlist=mnth.split('-')
    print(mnlist)
    mnth_num=mnlist[1]
    year_num=mnlist[0]
    print(mnth_num+"\n"+year_num)
    respdata={}
    datalist=[]
    ob1=Attendance_table.objects.filter(Usernm=empnm,Date__startswith=mnth_num,Date__endswith=year_num)
    for i in ob1:
        print(i.Usernm)
        data=[]
        ob2=Student_table.objects.get(Username=i.Usernm)
        name=ob2.Name
        dept=ob2.Batch
        print(name)
        print(i.Usernm)
        data.append(i.Date)
        data.append(i.Punchin)
        data.append(i.Punchout)
        data.append(i.Subject)
        datalist.append(data)
    print(datalist)
    respdata["datalist"]=datalist
    respdata["name"]=name
    respdata["dept"]=dept
    return JsonResponse(respdata,safe=False)







 

    
def Admin_view_salary(request):
    return render(request,'admin/view_salary.html',{})


def Admin_cap_img(request):
    return render(request,'admin/capimg.html',{})

import os
@csrf_exempt
def Getimage(request):
    imgdata=request.POST.get("imgdata")
    nim=request.POST.get("nim")
    print(nim)
    
    # print("imagedata==>",imgdata)
    try:
        
        imgdata = base64.b64decode(imgdata)
        filename = 'myimage.jpg'  
        with open(filename, 'wb') as f:
            f.write(imgdata)
        img = cv2.imread('myimage.jpg')
  
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw rectangle around the faces and crop the faces
        for (x, y, w, h) in faces:
            
            faces = img[y:y + h, x:x + w]
            cv2.imwrite('face.jpg', faces)
        data={"status":1}
        return JsonResponse(data,safe=False)
    except Exception as e:
        print(e)
        data={"status":0}
        return JsonResponse(data,safe=False)




def Student_view_attendance(request):
    return render(request,'student/student_attendance.html',{})

def student_get_attendance(request):
    name=""
    mnth=request.GET.get("mnth")
    empnm=request.session["usernm"]
    print(mnth+"\n"+empnm)
    mnlist=mnth.split('-')
    print(mnlist)
    mnth_num=mnlist[1]
    year_num=mnlist[0]
    print(mnth_num+"\n"+year_num)
    respdata={}
    datalist=[]
    ob1=Attendance_table.objects.filter(Usernm=empnm,Date__startswith=mnth_num,Date__endswith=year_num)
    for i in ob1:
        data=[]
        ob2=Student_table.objects.get(Username=i.Usernm)
        name=ob2.Name
        print(name)
        print(i.Usernm)
        data.append(i.Date)
        data.append(i.Punchin)
        data.append(i.Punchout)
        data.append(i.Subject)
        datalist.append(data)
    print(datalist)
    respdata["datalist"]=datalist
    respdata["name"]=name
    return JsonResponse(respdata,safe=False)





        



import os
def getfaceusid(request):
    uname=request.GET.get("userid")
    request.session["faceusid"]=uname
    print(uname)
    # capface(uname)
    data={"status":0}
    return JsonResponse(data,safe=False)

def getsaveface(request):
    uname=request.session["faceusid"]
    side=request.GET.get("side")
    print(uname)
    print(side)
    capface(uname,side)
    data={"status":0}
    return JsonResponse(data,safe=False)


