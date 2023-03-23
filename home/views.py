from django.shortcuts import render


# Using `home` as prefix folder for `index.html` to preserve `home` namespace.
def home(request):
    return render(
        request=request,
        template_name="home/index.html"
    )
