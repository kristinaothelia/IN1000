"""
IN1000 - Obligatorisk innlevering 5

Oppgave 3: Skop
"""

""" Programflyt

Forst defineres funksjonen minFunksjon(), denne tar ikke input/parametre.
Deretter lages prosedyren hovedprogram(), denne tar ikke input/parametre.
Naa kalles hovedprogram()

Her opprettes variablene a=42 og b=0. Deretter printes b (=0).
Saa settes b lik a, og a lik funksjonen minFunksjon()

Naar funksjonen blir kaldt paa settes en for-lokke med range 2 i gang.
Forst opprettes variabelen c=2, og denne printes (c=2).
Saa okes c med en verdi 1.
Deretter opprettes variabelen b=10. Denne skal saa okes med variabelen 'a'.
Problemet er at denne variabelen ikke er definert! og den er ikke input i
funksjonen. Altsaa klarer ikke programmet aa gjore denne linjekoden.
Programmet brytes.

Skulle ha skjedd dersom a var input i minFunksjon():

b skulle blitt addert med input variabelen, for saa aa bli printet og returnert
Tilbake i prosedyren, skulle a som kaller funksjonen faatt 'b' verdien som
returneres av funksjonen. Til slutt printes a og b inne i hovedprogrammet
"""


def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()
