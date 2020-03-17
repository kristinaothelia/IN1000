"""
IN1000 - Obligatorisk innlevering 5

Oppgave 4: Repetisjon


Dette programmet lager en tom liste som skal fylles opp med ord gitt av
brukeren. Vi har to funksjoner, slaaSammen() slaar sammen to bruker input
til ett ord,  og skrivUt() skriver ut listen med ord. Der den skriver ut
ett ord pr linje fra listen.
Vi bruker en while lokke som ber om ny input inntil man avslutter med 's'.
Andre spesialtegn er 'i'-ber om to input som slaas sammen av slaaSammmen() og
'u'-som skriver ut listen med ord.
Listen blir oppdatert hver gang programmet faar en input verdi av brukeren.

Note: Funker bare med py3
"""

# Tom liste
mineOrd = []

def slaaSmmen(a, b):
    return a + b

def skrivUt(list):

    for i in range(len(list)):
        print(list[i])

print("Spesial kommandoer: i, u og s (exit)")

ord_ = input("Skriv noe: ")

while ord_ != "s":
    mineOrd.append(ord_)
    ord_ = input("Skriv noe: ")
    if ord_ == "i":
        print("Spesialtegn: Skriv to ord som skal settes sammen")
        a  = input("Skriv streng 1: ")
        b  = input("Skriv streng 2: ")
        ab = slaaSmmen(a, b)
        print(ab)
        mineOrd.append(ab)
    if ord_ == "u":
        print("Spesialtegn: Skriver ut listen med ord")
        a = skrivUt(list=mineOrd)

print("--"*15)
print("Den endelige listen ble slik:")
print(skrivUt(list=mineOrd))
