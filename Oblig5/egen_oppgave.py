"""
IN1000 - Obligatorisk innlevering 5

Oppgave 5: Egen oppgave - Eksempelprogram

Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil
der hver linje beskriver et navn paa et maal og selve maalet i tommer

Skulderbredde 4
Halsvidde 3.2
Livvidde 10

La programmet legge disse maalene i en ordbok med navn paa maalet som
nokkelverdi og returner ordboken.
Lag deretter en prosedyre som tar imot en liste av maal og benytter seg av
tommerTilCm som du skrev tidligere for aa skrive ut maalene i centimeter
"""

def make_dictionary():

    minFil = open("skreddermaal.txt", "r")
    Ordbok = {}

    for line in minFil:
        # Split when space
        lines = line.split()

        # Set first element as description, second element as measurment
        beskrivelse = lines[0]
        tommer = lines[1]

        # Make dictionary
        Ordbok[beskrivelse] = tommer

    return Ordbok

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    cm = antallTommer * 2.54
    return cm

def skredder_maal_til_cm(Ordbok):

    for key, value in Ordbok.items():
        cm = tommerTilCm(antallTommer=float(value))
        print("%-15s: %-3g tommer tilsvarer %g cm" %(key, float(value), cm))


Ordbok = make_dictionary()
skredder_maal_til_cm(Ordbok)


"""
Skulderbredde  : 4   tommer tilsvarer 10.16 cm
Halsvidde      : 3.2 tommer tilsvarer 8.128 cm
Livvidde       : 10  tommer tilsvarer 25.4 cm
"""
