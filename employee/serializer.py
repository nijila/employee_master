from .models import Employee
from rest_framework import routers, serializers, viewsets


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'image',
            'email',
            'address',
            'phone',
            'created_at',

        )
        read_only_fields = ('id',)