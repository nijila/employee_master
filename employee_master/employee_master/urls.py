"""employee_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee import views
from employee.views import EmployeeViewSet
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls), name="api"),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/profile/',views.index.as_view(), name='home'),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('login/', views.login.as_view(), name='login'),   
    # path('home/',views.index.as_view(), name='home'),
    path('addorviewemployee/', views.CreateViewEmployee.as_view(),name='addorviewemployee'),
    path('saveemployee/', views.saveemployee, name='saveemployee')
    
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
