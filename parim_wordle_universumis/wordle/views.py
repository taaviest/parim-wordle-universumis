from django.shortcuts import render
from django.template import Library

from Sõnade_loend.valmis_sonad import sonastik
import random as r

# Create your views here.

def algus(request):
    sonade_arv = len(sonastik)-1
    mitmes = r.randint(0, sonade_arv)
    global oige_sona
    oige_sona  = list(sonastik.keys())[mitmes]
    print(oige_sona)
    """    taht1 = tahed[0]
    taht2 = tahed[1]
    taht3 = tahed[2]
    taht4 = tahed[3]
    taht5 = tahed[4]
    context = {
        "I_taht":taht1,
        "II_taht":taht2,
        "III_taht":taht3,
        "IV_taht":taht4,
        "V_taht":taht5,
    }"""
    return render(request, "wordle/pealeht.html")
def kontroll(request):
    global oige_sona
    sona = request.POST.get("taht1")+request.POST.get("taht2")+request.POST.get("taht3")+request.POST.get("taht4")+request.POST.get("taht1")
    if sona == oige_sona:
        return render(request, "wordle/pealeht.html", {"varv":"green"})
    else:
        return render(request, "wordle/pealeht.html", {"varv":"red", "sonum":"Proovi uuesti!"})

