from django.contrib import admin
from .models import User, Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('full_name',)
    pass

class UserAdmin(admin.ModelAdmin):
   pass

# Register the admin class with the associated model
admin.site.register(User, UserAdmin)
