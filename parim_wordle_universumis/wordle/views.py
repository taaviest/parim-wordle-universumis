from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.template import Library
from wordle.models import mang
from django.urls import reverse
from Sõnade_loend.valmis_sonad import sonastik
import random as r

# Create your views here.

def algus(request):
    global mangu_id
    sonade_arv = len(sonastik)-1
    mitmes = r.randint(0, sonade_arv)
    oige_sona  = list(sonastik.keys())[mitmes]
    uus_mang = mang(oige_sona=oige_sona, sona1="", sona2="",sona3="",sona4="",sona5="")
    uus_mang.save()
    mangu_id = uus_mang.id
    print(oige_sona)
    return render(request, "wordle/pealeht.html")

def kontroll(request):
    if request.method=="POST":
        global mangu_id
        sona = request.POST.get("taht1")+request.POST.get("taht2")+request.POST.get("taht3")+request.POST.get("taht4")+request.POST.get("taht5")
        mangu_objekt = mang.objects.get(id=mangu_id)
        oige_sona = mangu_objekt.oige_sona
        if sona == oige_sona:
            sonum="Oige!"
            return render(request, "wordle/pealeht.html", {"varv":"green", "sonum":sonum, "kas":True})
            mangu_objekt.delete()
        else:
            return render(request, "wordle/pealeht.html", {"varv":"red", "sonum":"Proovi uuesti!", "kas":False})
    elif request.method=="GET":
        return HttpResponseRedirect(reverse("algus"))