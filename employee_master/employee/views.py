from django.shortcuts import render
from django.views.generic import base
from django.views.decorators.csrf import csrf_exempt
from employee.models import User, Employee
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings 
import json
from rest_framework import viewsets
from .serializer import EmployeeSerializer
from django.shortcuts import render
from .employee_form import EmployeeCreateForm, EmployeeListForm


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()




# Create your views here.

class index(base.View):
    def post(self, request):
        return render(request, 'home.html',{})

    def get(self, request):
        return render(request, 'home.html',{})
    # def get(self, request):
    #     return render(request, 'base.html',{})

# class login(base.View):
#     def post(self, request):
#         # print(request.POST.get('username'))
#         # user_name = request.POST.get('username')
#         # password = request.POST.get('password')
#         # user=User.objects.get(username=str(user_name))
#         # # user = authenticate(username=str(user_name))
#         # print(user)
#         return render(request, 'home.html',{})

#     def get(self, request):
#         return render(request, 'home.html',{})

class CreateViewEmployee(base.View):
    def post(self, request):
        print(request)
        if request.POST.get("add"):
            form = EmployeeCreateForm(request.POST)
            if form.is_valid():
                pass 
            return render(request, 'create.html',{'form':form})
        else:
            objects = Employee.objects.all()
            context = {'employee': objects}
            return render(request, 'employeelist.html', context)
    
    def get(self, request):
        # employee = Employee.objects.get(id=employee_id)
        objects = Employee.objects.all
        context = {'employee': employee, 'objects': objects}
        return render(request, 'employeelist', context)
        # form = EmployeeListForm(request.POST)
        # if form.is_valid():
        #     pass 
        # return render(request, 'employeelist.html',{'form':form})

def saveemployee(request):
    if request.method == 'POST':
        
        form = EmployeeCreateForm(data=request.POST, files=request.FILES)
        # print(form.cleaned_data['image'])
        print("hello")
        print(form.errors)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/accounts/profile/')

# @csrf_exempt
# def login(request):
#     print(request.method )
#     if request.method == 'POST':
#         form = EmployeeCreateForm(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#             return render(request, 'base.html', {'form': form})
#     else:
#         return render(request, 'home.html', {'form': form})
    

# @csrf_exempt
# def login(request):
#     print("hellooo")
#     print(request.method)
#     client_ip = request.META['REMOTE_ADDR']
#     # try:
#     if request.method != 'POST':
#         return HttpResponseNotAllowed('Only POST here')
#     print(request.POST)
#     print(request.POST.get('Username'))
#     user_name = request.POST.get('Username')
#     password = request.POST.get('password')
#     hashed_password = make_password(password)
#     print(hashed_password)
#     # user=User.objects.get(username=str(user_name), password=str(hashed_password))
#     user = authenticate(username=str(user_name), password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/')
#     print("user found", user)
#     print(user_name)

#     return True