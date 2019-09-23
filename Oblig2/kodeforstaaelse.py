"""
Obligatorisk innlevering 2

Teori spm:
1.
Ja dette er en lovlig kode. Om man ser bort fra mellomrom-problemet etter print

a spør om input, noe brukeren maa gi. Input blir str
b gjor a om til en integer. Dette er lov
print burde gi <Heltall>Hei!

2.
En ulempe fra if-lokken er at man ikke vil faa en feilmelding om man setter
a hoyere enn 9, paa hvorfor ikke noe printes
"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")

""" Rettelser
Dette var ikke en gyldig kode.
Kan ikke slaa sammen et heltall og en tekststreng, med "+"

Vi maatte brukt:

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    b = str(b)
    print(b + "Hei!")
"""
