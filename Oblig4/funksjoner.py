"""
IN1000 - Obligatorisk innlevering 4

Oppgave 1: Parametere og returverdier

1)
Progrmmet har en funksjon med to variabler.
Disse variablene blir summert sammen i funskjonen og svaret returnert.
Kaller funksjonen to ganger, og bruker begge svarene i en print()
2)
Funksjonen tar inn to variabler, str. Den ene variablen testes mot den andre
i en for lokke. For hver bokstav i testes det om i er lik som bokstaven vi er
paa jakt etter. En counter teller opp hvor mange ganger dette slaar an.
Deretter printes resultatet.
"""

### 1

def adder(tall1, tall2):

    Sum = tall1 + tall2

    return Sum

Kall1 = adder(tall1=1, tall2=9)
Kall2 = adder(tall1=2, tall2=2)

print("1 + 9 blir: ", Kall1, " og 2 + 2 blir: ", Kall2)

### 2 og 3

def tellForekomst(minTekst, minBokstav):

    Bokstav_teller = 0                  # Teller variabel som starter paa 0

    for i in minTekst:
        if i == minBokstav:
            Bokstav_teller += 1         # Teller variabel teller +1 for hver
                                        # gang bokstaven er i string
    print("Bokstaven '%s' var %g ganger i teksten" %(minBokstav, Bokstav_teller))

tellForekomst(input("Skriv en tekst: "), input("Skriv en bokstav: "))
