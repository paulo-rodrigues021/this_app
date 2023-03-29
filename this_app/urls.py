# from django.contrib import admin
# from django.urls import path, include


# urlpatterns = [
#     path(route="admin/", view=admin.site.urls),
#     path(route="", view=include("home.urls")),
#     path(route="department/", view=include("department.urls")),
#     path(route="employee/", view=include("employee.urls")),
#     path(route="api/employee/", view=),
# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from department import views as department_view

# urlpatterns = [
#     path('snippets/', department_view.department_list),
#     path('snippets/<int:pk>/', department_view.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


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
    path("api/employee/", include(router.urls)),
    path("api/department/", department_view.department_list),
]
