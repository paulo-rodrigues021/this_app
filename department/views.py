from django.shortcuts import render

# Using `department` as prefix folder for `index.html` to preserve `department` namespace.
def index(request):
    return render(
        request=request,
        template_name="department/index.html"
    )
