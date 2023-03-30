from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DepartmentModel
from .serializers import DepartmentSerializer


# Using `department` as prefix folder for `index.html` to preserve `department` namespace.
def index(request):
    return render(
        request=request,
        template_name="department/list_view.html",
        context={
            "departments": DepartmentModel.objects.all()
        }
    )


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentView(APIView):
    ## Auth
    # from rest_framework import authentication, permissions
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        department_names = [department.name for department in DepartmentModel.objects.all()]
        return Response(department_names)

    def post(self, request):
        department_serializer = DepartmentSerializer(data=request.data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response(department_serializer.data, status=status.HTTP_201_CREATED)
        return Response(department_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name=None):
        department = DepartmentModel.objects.filter(name=name)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
