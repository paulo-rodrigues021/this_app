from django.db import models

from department.models import DepartmentModel


class EmployeeModel(models.Model):
    """ Using a lot of chars for names and emails is strongly recommended for systems
    that are going to be used all over the world. For a simple application we will keep
    char's lenght of 200 as standard.
    """

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.department)
