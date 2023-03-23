from django.shortcuts import render
from .models import DepartmentModel


# Using `department` as prefix folder for `index.html` to preserve `department` namespace.
def index(request):
    return render(
        request=request,
        template_name="department/index.html",
        context={
            "departments": DepartmentModel.objects.all()
        }
    )
