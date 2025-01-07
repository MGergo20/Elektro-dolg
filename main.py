import feladat

eredmeny=feladat.masodperc(59)
print(f"    59mp --> {eredmeny}")
eredmeny=feladat.masodperc(63)
print(f"    63mp --> {eredmeny}")
eredmeny=feladat.masodperc(125)
print(f"   125mp --> {eredmeny}")
eredmeny=feladat.masodperc(3672)
print(f"  3672mp --> {eredmeny}")
eredmeny=feladat.masodperc(11502)
print(f" 11502mp --> {eredmeny}")


masodpercek_szamolas=feladat.osszes_masodperc(0, 0, 59)
print(f"0ó, 0p, 59mp -->  {masodpercek_szamolas}mp")
masodpercek_szamolas=feladat.osszes_masodperc(0,1,3)
print(f"0ó, 1p, 3mp -->   {masodpercek_szamolas}mp")
masodpercek_szamolas=feladat.osszes_masodperc(0,2,5)
print(f"0ó, 2p, 5mp -->  {masodpercek_szamolas}mp")
masodpercek_szamolas=feladat.osszes_masodperc(1,1,12)
print(f"1ó, 1p,12mp --> {masodpercek_szamolas}mp", )
