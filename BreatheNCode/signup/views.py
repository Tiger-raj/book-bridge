from django.shortcuts import render
from django.http import HttpResponse

from signup.models import User
# Create your views here.

def index(request):
    return render(request,'index.html')

users=User.objects.all()