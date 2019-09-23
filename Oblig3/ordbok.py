"""
IN1000 - Obligatorisk innlevering 3

Oppgave 2: Ordbok
Lager en ordbok med en vare og tilhorende pris.
Deretter lar vi brukeren selv skrive inn to varer med pris, som vi
legger til i ordboken. Resten er print og lister funksjoner. 
"""

""" 1)
Lag en ordbok (dictionary) som skal inneholde varer i en butikk og pris.
Du skal bruke varenavn som nokkelverdier og varepriser (i form av flyttall)
som innholdsverdier. Opprett ordboka med folgende varer med tilhorende pris:
melk - kr 14.90, brod - kr 24.90, yoghurt - 12.90 og pizza - 39.90.
Skriv ut innholdet i ordboken med en enkel print-setning.
"""

Ordbok = {"melk": 14.90, "brod": 24.90, "yoghurt": 12.90, "pizza": 39.90}
print(Ordbok)

""" 2)
Les inn to varenavn og priser fra brukeren og legg disse til i ordboken.
Skriv ut ordboken på nytt.
"""

print("Skriv inn 2 matvarer med pris")
Vare = input("Skriv en matvare: ")
Pris = input("Skriv prisen paa matvaren: ")
Ordbok[Vare] = Pris
Vare = input("Skriv en matvare: ")
Pris = input("Skriv prisen paa matvaren: ")
Ordbok[Vare] = Pris
print(Ordbok)
