"""
IN1000 - Obligatorisk innlevering 4

Oppgave 4: Reiseplan

Denne oppgaven ber brukeren om 3 type input som lagres i 3 lister.
reiseplan listen inneholder disse 3 listene.
Videre spor vi brukeren om aa velge et element i reiseplan listen, ved aa
oppgi 2 indexer (i1 og i2).
Vi bruker en if-lokke til aa sjekke om inputet er gyldig, altsaa et gyldig tall
som representerer en index i listen. (I denne oppgaven vil reiseplan ha
shape(3,5)) Altsaa maa i1 vere mellom 0 og 2, og i2 mellom 0 og 4.
"""

n = 5

steder        = []
klesplagg     = []
avreisedatoer = []
reiseplan     = []  # Faar shape(3, n)

for i in range(n):
    steder.append(input("Oppgi et reisemaal: "))
for i in range(n):
    klesplagg.append(input("Pakkeliste! Oppgi et klesplagg: "))
for i in range(n):
    print("OBS! Det sjekkes ikke om det er en gyldig dato")
    avreisedatoer.append(input("Oppgi en avreisedato: (Eks 01.01.01) "))

reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

# Henter inn bruker input som gjores om til indexer senere
print("--"*10)

i1 = int(input("Velg en liste: (0=Sted, 1=Klesplagg, 2=Dato) "))
i2 = int(input("Velg et av 5 elementer i listen: (0-4) "))

if i1 <=(len(reiseplan)-1) and i1 >= 0:
    if i2 <= (n-1) and i2 >=0:
        print("Du valgte: ", reiseplan[i1][i2])
    else:
        print("Ugyldig i2 input")
else:
    print("Ugyldig i1 input")
    if i2 <= (n-1) and i2 >=0:
        print("Men gyldig i2 input")
    else:
        print("Og ugyldig i2 input")

""" Sample run for 5)
Oppgi et reisemaal: Bali
Oppgi et reisemaal: Cuba
Oppgi et reisemaal: Island
Oppgi et reisemaal: Oslo
Oppgi et reisemaal: Sverige
Pakkeliste! Oppgi et klesplagg: Bikini
Pakkeliste! Oppgi et klesplagg: Solbriller
Pakkeliste! Oppgi et klesplagg: Jakke
Pakkeliste! Oppgi et klesplagg: Genser
Pakkeliste! Oppgi et klesplagg: Lue
OBS! Det sjekkes ikke om det er en gyldig dato
Oppgi en avreisedato: (Eks 01.01.01) 01.01.20
OBS! Det sjekkes ikke om det er en gyldig dato
Oppgi en avreisedato: (Eks 01.01.01) 01.02.20
OBS! Det sjekkes ikke om det er en gyldig dato
Oppgi en avreisedato: (Eks 01.01.01) 01.07.20
OBS! Det sjekkes ikke om det er en gyldig dato
Oppgi en avreisedato: (Eks 01.01.01) 01.10.19
OBS! Det sjekkes ikke om det er en gyldig dato
Oppgi en avreisedato: (Eks 01.01.01) 99.99.01
--------------------
Velg en liste: (0=Sted, 1=Klesplagg, 2=Dato) 1
Velg et av 5 elementer i listen: (0-4) 2
Du valgte:  Jakke
"""
