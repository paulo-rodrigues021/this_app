from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from employee import views as employee_view
from department import views as department_view


# Serves the API
router = routers.DefaultRouter()
router.register(r'employee', employee_view.EmployeeViewSet)
router.register(r'department', department_view.DepartmentViewSet)


urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="", view=include("home.urls")),
    path(route="department/", view=include("department.urls")),
    path(route="employee/", view=include("employee.urls")),
    path("api/employee/", employee_view.EmployeeView.as_view()),
    path("api/department/", department_view.DepartmentView.as_view()),
]
