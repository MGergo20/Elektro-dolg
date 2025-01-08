from auto import Auto

def beolvas(fajlnev):
    autok = []
    with open(fajlnev, "r") as fajl:
        fajl.readline() 
        for sor in fajl:
            nev, ev = sor.strip().split("-")
            autok.append(Auto(nev, ev))
    return autok

def flotta(autok):
    return len(autok)

def atlageletkor(autok, ev=2025):
    osszeg = 0
    szamlalo = 0
    for auto in autok:
        osszeg += ev - auto.gyartasi_ev  
        szamlalo += 1  
    if szamlalo == 0:  
        return 0
    return osszeg / szamlalo  