from django.shortcuts import render
from django.template import Library
from Sõnade_loend.valmis_sonad import sonastik
import random as r

# Create your views here.

def pealeht(request):
    sonade_arv = len(sonastik)-1
    mitmes = r.randint(0, sonade_arv)
    tahed = sonastik[list(sonastik.keys())[mitmes]]
    taht1 = tahed[0]
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
    }
    return render(request, "wordle/pealeht.html", context)

