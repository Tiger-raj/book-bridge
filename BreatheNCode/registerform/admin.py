from django.contrib import admin
from django.contrib.admin.sites import site
from registerform.models import Userdetail,Userfulldetail

class RegisterUser(admin.ModelAdmin):
    list_display1=('first_name','username','user_email','user_password')
admin.site.register(Userdetail,RegisterUser)

class RegisterfullUser(admin.ModelAdmin):
    list_display2=('first_name','username','user_email','user_password','user_year','user_course','user_phone','user_reg_no','user_gender')
admin.site.register(Userfulldetail,RegisterfullUser)

# Register your models here.
