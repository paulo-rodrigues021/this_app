from django.db import models


class DepartmentModel(models.Model):

    # Our UUID lib uses 22 chars. We are using 25 to be carefull
    id = models.CharField(max_length=25, primary_key=True, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.id, self.name)