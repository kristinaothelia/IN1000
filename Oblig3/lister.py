"""
IN1000 - Obligatorisk innlevering 3

Oppgave 1: Lister
Dette programmet tar for seg ulike kommandoer man kan gjore med en liste.
Lage lister, legge til elementer, sjekke om en verdi er i listen, og bruke
sum/produkt paa lister som inneholder tall.
"""

import numpy as np

""" 1) """

Liste = [2,4,6]     # Liste med 3 tall
Liste.append(8)     # Legger til tallet 8 bakerst i listen
print("First and third number in list: ", Liste[0], " and ", Liste[2])

""" 2) """

Navn = []           # Tom liste

print("\n","Skriv inn 4 navn :)")
Navn.append(input("Navn 1: "))
Navn.append(input("Navn 2: "))
Navn.append(input("Navn 3: "))
Navn.append(input("Navn 4: "))
print("Listen med navn: ", Navn)

""" 3) """

if "Kristina" in Navn:
    print("Du husket meg!", "\n")
else:
    print("Glemte du meg?", "\n")

""" 4) """
Sum_liste  = np.sum(Liste)    # 20
Prod_liste = np.prod(Liste)   # 384
Ny_liste   = [Sum_liste, Prod_liste]
print(Ny_liste)
Tot_liste  = Liste + Ny_liste
print(Tot_liste)
Tot_liste  = Tot_liste[:-2]
print(Tot_liste)
