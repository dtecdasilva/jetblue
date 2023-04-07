from django.shortcuts import render
from django.http import HttpResponse
from .models import Package


def index(request):
    packages = Package.objects.all()
    return render(request, 'index.html', {'packages': packages})


def searchbar(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            packages = Package.objects.filter(shipped_id__contains=query)
            return render(request, 'search.html', {'packages': packages})
        else:
            print("no info to show")
            return render(request, 'search.html', {})
