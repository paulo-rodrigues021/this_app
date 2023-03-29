from django.db import models


class DepartmentModel(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.name)