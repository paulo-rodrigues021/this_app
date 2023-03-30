from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmployeeModel
from .serializers import EmployeeSerializer


# Using `employee` as prefix folder for `index.html` to preserve `employee` namespace.
def index(request):
    return render(
        request=request,
        template_name="employee/list_view.html",
        context={
            "employees": EmployeeModel.objects.all()
        }
    )


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(APIView):
    ## Auth
    # from rest_framework import authentication, permissions
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        employees = EmployeeModel.objects.all().values()
        return Response(employees)

    def post(self, request):
        employee_serializer = EmployeeSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email=None):
        employee = EmployeeModel.objects.filter(email=email)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

