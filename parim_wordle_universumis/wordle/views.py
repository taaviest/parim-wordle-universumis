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
    global mitmes
    mitmes = 1
    sonade_arv = len(sonastik)-1
    mitmes = r.randint(0, sonade_arv)
    oige_sona  = list(sonastik.keys())[mitmes]
    uus_mang = mang(oige_sona=oige_sona, sona1="     ", sona2="     ",sona3="     ",sona4="     ",sona5="     ")
    uus_mang.save()
    mangu_id = uus_mang.id
    print(oige_sona)
    mangu_objekt = uus_mang
    context = {
            "taht1_1": list(mangu_objekt.sona1)[0],
            "taht1_2": list(mangu_objekt.sona1)[1],
            "taht1_3": list(mangu_objekt.sona1)[2],
            "taht1_4": list(mangu_objekt.sona1)[3],
            "taht1_5": list(mangu_objekt.sona1)[4],
            "taht2_1": list(mangu_objekt.sona2)[0],
            "taht2_2": list(mangu_objekt.sona2)[1],
            "taht2_3": list(mangu_objekt.sona2)[2],
            "taht2_4": list(mangu_objekt.sona2)[3],
            "taht2_5": list(mangu_objekt.sona2)[4],
            "taht3_1": list(mangu_objekt.sona3)[0],
            "taht3_2": list(mangu_objekt.sona3)[1],
            "taht3_3": list(mangu_objekt.sona3)[2],
            "taht3_4": list(mangu_objekt.sona3)[3],
            "taht3_5": list(mangu_objekt.sona3)[4],
            "taht4_1": list(mangu_objekt.sona4)[0],
            "taht4_2": list(mangu_objekt.sona4)[1],
            "taht4_3": list(mangu_objekt.sona4)[2],
            "taht4_4": list(mangu_objekt.sona4)[3],
            "taht4_5": list(mangu_objekt.sona4)[4],
            "taht5_1": list(mangu_objekt.sona5)[0],
            "taht5_2": list(mangu_objekt.sona5)[1],
            "taht5_3": list(mangu_objekt.sona5)[2],
            "taht5_4": list(mangu_objekt.sona5)[3],
            "taht5_5": list(mangu_objekt.sona5)[4],
        }
    return render(request, "wordle/pealeht.html", context)

def kontroll(request):
    if request.method=="POST":
        global mitmes
        global mangu_id
        sona = request.POST.get("taht1")+request.POST.get("taht2")+request.POST.get("taht3")+request.POST.get("taht4")+request.POST.get("taht5")
        mangu_objekt = mang.objects.get(id=mangu_id)
        oige_sona = mangu_objekt.oige_sona
        if mitmes == 1:
            mangu_objekt.sona1 = sona
            mangu_objekt.save()
        elif mitmes == 2:
            mangu_objekt.sona2 = sona
            mangu_objekt.save()
        elif mitmes == 3:
            mangu_objekt.sona3 = sona
            mangu_objekt.save()
        elif mitmes == 4:
            mangu_objekt.sona4 = sona
            mangu_objekt.save()
        elif mitmes == 5:
            mangu_objekt.sona5 = sona
            mangu_objekt.save()
        mitmes += 1
        context = {
            "taht1_1": list(mangu_objekt.sona1)[0],
            "taht1_2": list(mangu_objekt.sona1)[1],
            "taht1_3": list(mangu_objekt.sona1)[2],
            "taht1_4": list(mangu_objekt.sona1)[3],
            "taht1_5": list(mangu_objekt.sona1)[4],
            "taht2_1": list(mangu_objekt.sona2)[0],
            "taht2_2": list(mangu_objekt.sona2)[1],
            "taht2_3": list(mangu_objekt.sona2)[2],
            "taht2_4": list(mangu_objekt.sona2)[3],
            "taht2_5": list(mangu_objekt.sona2)[4],
            "taht3_1": list(mangu_objekt.sona3)[0],
            "taht3_2": list(mangu_objekt.sona3)[1],
            "taht3_3": list(mangu_objekt.sona3)[2],
            "taht3_4": list(mangu_objekt.sona3)[3],
            "taht3_5": list(mangu_objekt.sona3)[4],
            "taht4_1": list(mangu_objekt.sona4)[0],
            "taht4_2": list(mangu_objekt.sona4)[1],
            "taht4_3": list(mangu_objekt.sona4)[2],
            "taht4_4": list(mangu_objekt.sona4)[3],
            "taht4_5": list(mangu_objekt.sona4)[4],
            "taht5_1": list(mangu_objekt.sona5)[0],
            "taht5_2": list(mangu_objekt.sona5)[1],
            "taht5_3": list(mangu_objekt.sona5)[2],
            "taht5_4": list(mangu_objekt.sona5)[3],
            "taht5_5": list(mangu_objekt.sona5)[4],
        }
        if sona == oige_sona:
            sonum="Õige!"
            return render(request, "wordle/pealeht.html", {"varv":"green", "sonum":sonum, "kas":True}.update(context))
            mangu_objekt.delete()
        else:
            return render(request, "wordle/pealeht.html", {"varv":"red", "sonum":"Proovi uuesti!", "kas":False}.update(context))
    elif request.method=="GET":
        return HttpResponseRedirect(reverse("algus"))