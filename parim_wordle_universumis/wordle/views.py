from django.shortcuts import render

# Create your views here.

def pealeht(request):
    return render(request, "pealeht.html")