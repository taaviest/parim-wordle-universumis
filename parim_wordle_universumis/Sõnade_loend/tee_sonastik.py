f1 = open("sonad.txt", "r", encoding="ansi")
f2 = open("valmis_sonad.py", "w", encoding="utf-8")
tekst = f1.readlines()
sonade_list = []
for rida in tekst:
    rida = rida.strip().lower()
    if len(rida) == 5 and "-" not in rida:
        sonade_list.append(rida)
f2.write("sonade_list = "+str(sonade_list))
f1.close()
f2.close()
