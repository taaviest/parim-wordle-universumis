from django.shortcuts import render
from django.template import Library

# Create your views here.

def pealeht(request):
    return render(request, "wordle/pealeht.html")