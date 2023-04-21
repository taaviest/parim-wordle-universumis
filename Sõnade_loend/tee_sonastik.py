f1 = open("sonad.txt", "r", encoding="ansi")
f2 = open("valmis_sonad.txt", "w", encoding="utf-8")
tekst = f1.readlines()
sonastik = {}
for rida in tekst:
    rida = rida.strip().lower()
    if len(rida) == 5 and "-" not in rida:
        sonastik[rida]=list(rida)
mitu_sona = len(sonastik)
f2.write("sonastik = "+str(sonastik)+"\nmitu_sona = "+str(mitu_sona))
f1.close()
f2.close()
