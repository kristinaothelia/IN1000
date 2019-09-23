"""
Obligatorisk innlevering 1

Progmmet variabler.py gjor en rekke smaa oppgaver som inkluderer bruk av
variabler, print og input funksjoner
"""


""" Deloppgave 2 """

print("Hei Student!")

""" Deloppgave 3 """

navn = input("Skriv inn navnet ditt: ")
print("Hei ", navn)

""" Deloppgave 4 """

x = 4
y = 3

print(x)
print(y)
#print(x, "\n", y)   # Tallene kommer ikke direkte over hverandre

""" Deloppgave 5 """

Diff = x - y  # Trekker variablene fra hverandre
print("Differanse: ", Diff)

""" Deloppgave 6 """

nytt_navn = input("Gi et nytt navn: ")
sammen    = navn + nytt_navn  # Legger sammen variblene
print(sammen)

""" Deloppgave 7 """

sammen = navn + " og " + nytt_navn  # Legger inn en tekst mellom variablene
print(sammen)


""" Sample run
(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000>python variabler.py
Hei Student!
Skriv inn navnet ditt: k
Hei  k
4
3
Differanse:  1
Gi et nytt navn: j
kj
k og j
"""
