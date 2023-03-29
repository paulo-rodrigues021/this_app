from rest_framework import viewsets
from django.shortcuts import render

from .models import EmployeeModel
from .serializers import EmployeeSerializer


# Using `employee` as prefix folder for `index.html` to preserve `employee` namespace.
def index(request):
    return render(
        request=request,
        template_name="employee/index.html"
    )


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
