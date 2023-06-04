from urllib.request import HTTPRedirectHandler
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.template import Library
from wordle.models import mang
from django.urls import reverse
from Sõnade_loend.valmis_sonad import sonade_list
import random as r

# Create your views here.

def algus(request):
    global mangu_id
    global mitmes
    mitmes = 1
    sonade_arv = len(sonade_list)-1
    mitmes_suvaline = r.randint(0, sonade_arv)
    oige_sona  = sonade_list[mitmes_suvaline]
    uus_mang = mang(oige_sona=oige_sona)
    uus_mang.save()
    mangu_id = uus_mang.id
    print(uus_mang)
    return render(request, "wordle/pealeht.html")

def kontroll(request):
    if request.method=="POST":
        global mitmes
        global mangu_id
        print(mitmes)
        sona = request.POST.get("taht1")+request.POST.get("taht2")+request.POST.get("taht3")+request.POST.get("taht4")+request.POST.get("taht5")
        mangu_objekt = mang.objects.get(id=mangu_id)
        oige_sona = mangu_objekt.oige_sona
        #salvesta sona vastavalt mitmes on ning leia oiged varvid kastide jaoks
        if mitmes == 1:
            if sona in sonade_list:
                mangu_objekt.sona1 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona1:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "green")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "yellow")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "grey")
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 2:
            if sona in sonade_list:
                mangu_objekt.sona2 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona2:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona2_varv).insert(mitmes_taht, "green")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona2_varv).insert(mitmes_taht, "yellow")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona2_varv).insert(mitmes_taht, "grey")
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 3:
            if sona in sonade_list:
                mangu_objekt.sona3 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona1:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "green")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "yellow")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "grey")
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 4:
            if sona in sonade_list:
                mangu_objekt.sona4 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona1:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "green")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "yellow")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "grey")
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        elif mitmes == 5:
            if sona in sonade_list:
                mangu_objekt.sona5 = list(sona)
                mangu_objekt.save()
                mitmes_taht = 0
                for taht in mangu_objekt.sona1:
                    if taht == list(oige_sona)[mitmes_taht]:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "green")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    elif taht in list(oige_sona):
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "yellow")
                        mangu_objekt.save()
                        mitmes_taht += 1
                    else:
                        (mangu_objekt.sona1_varv).insert(mitmes_taht, "grey")
                        mangu_objekt.save()
                        mitmes_taht += 1
            else:
                sona_pole = True
        else:
            print("MITMES ON KATKI - väärtus: "+str(mitmes))

        #teeb listid tahtede ja varvidega
        sona1 = (mangu_objekt.sona1).extend(mangu_objekt.sona1_varv)
        sona2 = (mangu_objekt.sona2).extend(mangu_objekt.sona2_varv)
        sona3 = (mangu_objekt.sona3).extend(mangu_objekt.sona3_varv)
        sona4 = (mangu_objekt.sona4).extend(mangu_objekt.sona4_varv)
        sona5 = (mangu_objekt.sona5).extend(mangu_objekt.sona5_varv)

        if sona_pole:
            sonum = "Sellist eestikeelset sõna meil pole, proovi mõnda teist!"

        context = {
            "sona1": sona1,
            "sona2": sona2,
            "sona3": sona3,
            "sona4": sona4,
            "sona5": sona5,
            "sonum": sonum,
        }
        if sona == oige_sona:
            return render(request, "wordle/pealeht.html", context)
            mangu_objekt.delete()
        else:
            return render(request, "wordle/pealeht.html", context)
    elif request.method=="GET":
        return HttpResponseRedirect(reverse("algus"))