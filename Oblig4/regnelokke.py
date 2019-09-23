"""
IN1000 - Obligatorisk innlevering 4

Oppgave 2: Regning med lokker

Programmet ber brukeren om en rekke tall, som saa lagres i en liste. Denne
listen brukes i diverse while og for lokker for aa hente ut forskjellig
informasjon. Ved aa trykke '0' vil while lokken breake, og ikke lengre be
brukeren om nye tall.

Note:
Usikker på om 0 skal vere en del av listen eller ikke, men siden det er et tall
som blir tastet inn, tas det med.
"""

Input  = int(input("Skriv et heltall: "))
Liste  = []                                      # Tom liste
minSum = 0

while Input != 0:
    print(Input)
    Liste.append(Input)
    Input = int(input("Skriv et nytt heltall: "))
    if Input == 0:
        print("'0' endte programmet :)")
        Liste.append(Input)
        break

print("Listen med tall brukeren brukte: ", Liste)

for i in Liste:
    print(i)

for i in Liste:
    minSum += i

print("Den totale summen av tallene er: ", minSum)

Min = Liste[0]      # Random tall. Bruke [0] siden den maa fylles
Max = Liste[0]      # Random tall

# Bruker if lokker inni for lokken for aa sjekke om verdiene i listen
# er mindre/storre enn et gitt tall. Dette tallet oppfateres derfor if-lokken
# er True.

for i in range(len(Liste)):
    if Liste[i] < Min:
        #print("Mindre")
        Min = Liste[i]
    #else:
    #    print("Ikke mindre")
print("Min: ", Min)

for i in range(len(Liste)):
    if Liste[i] > Max:
        #print("Storre")
        Max = Liste[i]
    #else:
    #    print("Ikke mindre")
print("Max: ", Max)

### Sjekk
print("Min sjekk: ", min(Liste))
print("Max sjekk: ", max(Liste))
