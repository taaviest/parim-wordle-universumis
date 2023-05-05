from django.shortcuts import render
from django.template import Library
from Sõnade_loend.valmis_sonad import sonastik

# Create your views here.

def pealeht(request):
    context = {
        "sonad":sonastik
    }
    return render(request, "wordle/pealeht.html", context)