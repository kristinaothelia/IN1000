"""
IN1000 - Obligatorisk innlevering 3

Oppgave 3: Billettpris
Vi lager en funkjson som tar alder som input (definert av bruker).
Lager en if-lokke som sjekker hvilken billettkategori den gitte alderen
befinner seg i. Billettprisen til kategorien skrives ut.
"""


def Billettpris(alder):

    if alder <= 17:
        billettpris = 30
        print("Barnebillett. Pris: %0.1f kr." % billettpris)
    elif alder > 17 and alder < 63:
        billettpris = 50
        print("Voksenbillett. Pris: %0.1f kr." % billettpris)
    elif alder >= 63:
        billettpris = 35
        print("pensjonistbillett. Pris: %0.1f kr." % billettpris)

for i in range(4):
    Billettpris(alder=int(input("Skriv inn alderen din: ")))

""" Kommentar
Man kan eks bare skrive inn alder som tallverdi. Hvis man skriver "10" vil
programmet kutte.
En annen ting som blir feil er flyttall, saa man kan ikke skrive inn
at man er 12.5 aar. Dette er fordi vi bruker int(input())
"""

""" Sample run
Skriv inn alderen din: 12
Barnebillett. Pris: 30.0 kr.
Skriv inn alderen din: 17
Barnebillett. Pris: 30.0 kr.
Skriv inn alderen din: 50
Voksenbillett. Pris: 50.0 kr.
Skriv inn alderen din: 63
pensjonistbillett. Pris: 35.0 kr.
"""
