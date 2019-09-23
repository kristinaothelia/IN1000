"""
Obligatorisk innlevering 2

Funksjonen Informasjon() ber brukeren om navn og adresse, og skriver ut en
kort hilsen. Dette er gjort med input() og print() av tekst og string.
"""

def Informasjon():
    navn    = input("Skriv inn navn: ")
    adresse = input("Hvor kommer du fra? ")

    print("Hei, %s! Du er fra %s" %(navn, adresse))

def Linje():
    # Printer ut en tom Linje
    print()

""" Kaller funksjonene slik at vi faar riktig format paa utskriften """
Informasjon(); Linje(); Informasjon(); Linje(); Informasjon()

""" Sample run
(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000\Oblig2>python utskriftsfunksjon.py
Skriv inn navn: Espen Askeladd
Hvor kommer du fra? Oslo
Hei, Espen Askeladd! Du er fra Oslo

Skriv inn navn: Donald Duck
Hvor kommer du fra? Andeby
Hei, Donald Duck! Du er fra Andeby

Skriv inn navn: Minni Mus
Hvor kommer du fra? Museby
Hei, Minni Mus! Du er fra Museby
"""
