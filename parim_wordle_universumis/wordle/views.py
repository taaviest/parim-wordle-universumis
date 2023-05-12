from django.shortcuts import render
from django.template import Library
from Sõnade_loend.valmis_sonad import sonastik
import random as r

# Create your views here.

def pealeht(request):
    sonade_arv = len(sonastik)
    context = {
        "sonad":sonastik
    }
    return render(request, "wordle/pealeht.html", context)

