import time

def masodperc(masodperc):
    ora = masodperc // 3600  
    masodperc = masodperc % 3600  
    perc = masodperc // 60  
    masodperc = masodperc % 60 
    
    return f"{ora:02}:{perc:02}:{masodperc:02}"


def osszes_masodperc(ora, perc, masodperc):
    return ora * 3600 + perc * 60 + masodperc