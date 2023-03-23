from django.shortcuts import render


# Using `employee` as prefix folder for `index.html` to preserve `employee` namespace.
def index(request):
    return render(
        request=request,
        template_name="employee/index.html"
    )
