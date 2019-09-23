"""
IN1000 - Obligatorisk innlevering 4

Oppgave 5: Aa telle bokstaver og ord

Vi lager to funskjoner, Bokstaver og Ordbok. Bokstaver tar et ord som input,
der vi bruker en for-lokke for aa splitte opp ordet og telle antall bokstaver.
Returnerer saa antall bokstaver.
Ordbok tar en setning som input. Setningen splittes opp ord for ord og legges
i en ny liste. Vi tar saa aa legger til hvert ord i listen i en ordbok ved
bruk av en for-lokke. I tillegg bruker vi en if-lokke som sjekker om ordet
allerede ligger i listen. Hvis det gjor det, telles ordet flere ganger
(innholdsverdi i ordboken).
Til slutt brukes en if-else lokke for aa gi den rette printen, der vi bruker
key og value hentet fra ordboken i en for lokke.
"""

def Bokstaver(Ord):

    Bokstaver = 0
    for i in Ord:
        Bokstaver += 1

    return Bokstaver

def Ordbok(Setning):

    Ord = Setning.split()
    print("Det er %g ord i setningen din :)" % len(Ord))

    Ordbok = {}
    for word in Ord:

        if word not in Ordbok:
            Ordbok[word] = 1
        elif word in Ordbok:
            Ordbok[word] += 1

    print("men bare %g ulike ord!" % len(Ordbok))

    return Ordbok

Setning_fra_bruker = input("Skriv en setning: ")
Output             = Ordbok(Setning=Setning_fra_bruker)

for key, value in Output.items():

    noe = "forekommer"

    if value == 1:
        if Bokstaver(Ord=key) == 1:
            print("Ordet %15s forekommer %g gang, og har %g bokstav" % (key, value, Bokstaver(Ord=key)))
        else:
            print("Ordet %15s forekommer %g gang, og har %g bokstaver" % (key, value, Bokstaver(Ord=key)))
    else:
        if Bokstaver(Ord=key) == 1:
            print("Ordet %15s forekommer %g ganger, og har %g bokstav" % (key, value, Bokstaver(Ord=key)))
        else:
            print("Ordet %15s forekommer %g ganger, og har %g bokstaver" % (key, value, Bokstaver(Ord=key)))

""" Sample run
Skriv en setning: hei hei hei heeeeeeeeeei !
Det er 5 ord i setningen din :)
men bare 3 ulike ord!
Ordet             hei forekommer 3 ganger, og har 3 bokstaver
Ordet    heeeeeeeeeei forekommer 1 gang, og har 12 bokstaver
Ordet               ! forekommer 1 gang, og har 1 bokstav
"""
