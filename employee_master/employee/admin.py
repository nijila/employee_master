from django.contrib import admin
from .models import User, Employee

# Register your models here.
#Define the admin class
class UserAdmin(admin.ModelAdmin):
   pass

# Register the admin class with the associated model
admin.site.register(User, UserAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Employee, EmployeeAdmin)