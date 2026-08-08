from django.shortcuts import render,HttpResponse,redirect
from myapp.models import contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from subprocess import run,PIPE
import sys
from deepface import DeepFace
import csv
import cv2
import matplotlib.pyplot as plt

from myapp.forms import ImgsaveForm
from myapp.models import Imgsave1
from myapp.functions import handel_phot
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    
    return render(request,"index.html")

def opencamero(request):
   data=run([sys.executable,'C:/Users/ashis/AppData/Local/Programs/Python/Python36/facialExpression/emotion/myapp/templates/fi.py'],shell=False,stdout=PIPE)
   return render(request,'index.html',{'data':data.stdout})

def svimg(request):

    if request.method=='POST':
        img=ImgsaveForm(request.POST,request.FILES)
        if img.is_valid():
        
            handel_phot(request.FILES['file1'])
            model_instance=img.save(commit=False)
            model_instance.save()  
        
            show=Imgsave1.objects.all()
        return render(request,'upload.html',{'stu':show})
    else:
        img=ImgsaveForm()
        return render(request,"photoviewes.html",{
            'form':img
        })

def viewimg(request):
    show=Imgsave1.objects.all()
    return render(request,'upload.html',{'stu':show})

def destroy(request, id):  
    imgsv = Imgsave1.objects.get(id=id)  
    imgsv.delete()  
    return render(request,"upload.html",{'imgsv':imgsv})

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        cont=contact(name=name,phone=phone,email=email,desc=desc)
        cont.save()
    
    return render(request,"contactus.html")

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
  
    writer = csv.writer(response)
    writer.writerow(['id','name', 'file1', 'value'])
  
    users = Imgsave1.objects.all().values_list('id','name', 'file1', 'value')
    for user in users:
        writer.writerow(user)
 
    return response

def handlesignup(request):
    
    if request.method=='POST':
        fname=request.POST['fname']
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        conpassword=request.POST['conpassword']
        send_mail(
            'Facial Expression',
            'You have been successfully register.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        if len(username)>10:
            messages.error(request, "Username must be under 10 character")
            return redirect('myapp')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain letter and character")
            return redirect('myapp')


        if password!=conpassword:
            messages.error(request, "Password do not match")
            return redirect('myapp')

    


        myuser=User.objects.create_user(username,email,password)
        myuser.fullname=fname
        myuser.save()
        messages.success(request, "Successfully creater")
        return redirect('myapp')
    else:
        return HttpResponse('page not found')

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('myapp')
        else:
            messages.error(request,"invalid credentials, please try again")
            return redirect('myapp')

    return HttpResponse('404 - page not found')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('myapp')
    
def changepass(request):
    if request.method=='POST':
        newpass=request.POST.get('newpass')
        confirmpass=request.POST['confirmpass']
        if newpass!=confirmpass:
            messages.error(request, "Password do not match")
            return redirect('myapp')

        
        u=User.objects.get(username=request.user.username)
        u.set_password(newpass)
        u.save()
        messages.success(request, "Successfully password changed")
        return redirect('myapp')

