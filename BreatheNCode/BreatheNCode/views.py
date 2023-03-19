from django.http import HttpResponse
from django.shortcuts import render,redirect
from registerform.models import Userdetail,Userfulldetail

def HomePage(request):
    return render(request,'Home.html')

def login(request):
    return render(request,'login.html')

def saveform(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        username=request.POST.get('username')
        user_email=request.POST.get('user_email')
        user_password1=request.POST.get('user_password1')
        user_password2=request.POST.get('user_password2')
        enn=Userdetail(first_name=first_name,username=username,user_email=user_email,user_password=user_password1)
        enn.save()
        data={'fname':first_name,'uname':username,'uemail':user_email,'upassword1':user_password1}
        return render(request,"dashboard.html",data)

def submit(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        username=request.POST.get('username')
        user_email=request.POST.get('user_email')
        user_course=request.POST.get('user_course')
        user_year=request.POST.get('user_year')
        user_phone=request.POST.get('user_phone')
        user_reg_no=request.POST.get('user_reg_no')
        user_gender=request.POST.get('user_gender')
        dett=Userfulldetail(first_name=first_name,username=username,user_email=user_email,user_course=user_course,user_year=user_year,user_phone=user_phone,user_reg_no=user_reg_no,user_gender=user_gender)
        dett.save()
        data={'fname':first_name,'uname':username,'uemail':user_email,'ucourse':user_course,'uyear':user_year,'uphone':user_phone,'urno':user_reg_no,'ugender':user_gender}
        return render(request,'dashboard.html',data)
    else:
        pass
    
def books(request):
    return render(request,'books.html')

def dashboard(request):
    return render(request,'dashboard.html')

def nbooks(request):
    return render(request,'nbooks.html')

def fbooks(request):
    return render(request,'fbooks.html')