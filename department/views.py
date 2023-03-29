from rest_framework import viewsets
from django.shortcuts import render

from .models import DepartmentModel
from .serializers import DepartmentSerializer


# Using `department` as prefix folder for `index.html` to preserve `department` namespace.
def index(request):
    return render(
        request=request,
        template_name="department/index.html",
        context={
            "departments": DepartmentModel.objects.all()
        }
    )


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def department_list(request):

    if request.method == 'GET':
        snippets = DepartmentModel.objects.all()
        serializer = DepartmentSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)