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

def atlageletkor(autok, ):
    
