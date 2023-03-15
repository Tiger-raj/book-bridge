from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method =='POST':
        user_name=request.POST['user_name']
        email=request.POST['email']
        passward1=request.POST['passward1']
        passward2=request.POST['passward2']
        if passward1==passward2:
            if User.objects.filter(user_name=user_name).exist():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exist():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                User=User.objects.create_user(user_name=user_name,email=email,passward=passward1)
                User.save();
                print('user created')
                return redirect('register')
        else:
            print('passward not matched')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':

        user_name=request.POST['user_name']
        passward=request.POST['passward']
        user=auth.authenticate(user_name=user_name,passward=passward)
        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentails')
            return redirect('register')
    else:
        return render(request,"register.html")