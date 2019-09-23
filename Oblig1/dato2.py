"""
Obligatorisk innlevering 1 - Frivillig

Progmmet dato2.py utforer en rekke if-tester for aa bestemme hvilken av to input
datoer som skrives inn forst. Her har hver dato kun en variabel
"""

d1 = input("Dato 1. Skriv som mmdd ")
d2 = input("Dato 2. Skriv som mmdd ")

if d1 < d2:
    print("Riktig rekkefolge!")
elif d1 == d2:
    print("Samme dato!")
else:
    print("Feil rekkefolge")
