"""
Obligatorisk innlevering 2 - Egen oppgave

Oppgavetekst:

    Konsert

    a) Konsert billetter

    Skriv et programm som spor en bruker om hvor mange som skal paa en konsert.
    Spor deretter hvor mange billetter de trenger. Sjekk om antall personer
    som skal paa konserten samsvarer med antall billetter de onsker aa bestille.
    Gi en tilbakemelding.

    b) Konsert bakgrunnsinformasjon

    Spor brukeren om de har sett dette bandet/artisten tidligere.
    Gi en tilbakemelding.

    c) Ranger en tidligere konsert

    Ranger en tidligere konsertopplevelse med et terningkast.
    Pass paa aa gi en tilbakemelding om man svarer noe annet enn 1-6.

"""


def Konsert():

    """ a) Tester om antall konsertgaaere samsvarer med antall billetter. """

    Personer = int(input("Saa goy at dere skal paa konsert. Hvor mange personer skal dra? "))  # Maa ha int for aa teste tallene fra de to inputene mot hverandre
    Billetter = int(input("Dere er %g personer som skal på konsert. Hvor mange billetter trenger dere? " % Personer))

    if Billetter < Personer:
        print("OBS! Dette er for faa billetter")
    elif Billetter == Personer:
        print("Helt korrekt! Kos dere paa konsert")
    elif Billetter > Personer:
        print("Dette er for mange billetter. Prov aa selg noen, eller finn flere konsertdeltakere =D")
    else:
        print("huh..!?")  # Denne virker ikke pga tekst ikke blir omgjort til int

    """ b) """

    print("")
    print("Vi vil gjerne at du svarer paa noen spm ang konserter. Vennligst bruk smaa bokstaver i svarene.")

    Info = input("1. Har du sett dette bandet/artisten paa konsert tidligere? ")

    if Info == "ja":
        print("Da maa det vere en bra konsert!")
    elif Info == "nei":
        print("Alltid goy med nye konsertopplevelser =D")
    else:
        print("huh..!?")

    """ c) """

    Artist    = input("2. Hva var den forrige konserten du var paa? ")
    Rangering = int(input("3. Ranger %s konserten med ett terningkast " % Artist))  # Maa vere int

    if Rangering < 3 and Rangering >= 1:
        print("Det var synd at konserten var daarlig :/")
    elif Rangering >= 3 and Rangering < 5:
        print("Det er ikke heelt galt :)")
    elif Rangering >= 5 and Rangering <= 6:
        print("Fantastisk!")
    else:
        print("Ett terningkast er fra 1-6 :)")


Konsert()

""" Sample run

(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000\Oblig2>python Egen_oppgave.py
Saa goy at dere skal paa konsert. Hvor mange personer skal dra? 5
Dere er 5 personer som skal på konsert. Hvor mange billetter trenger dere? 5
Helt korrekt! Kos dere paa konsert

Vi vil gjerne at du svarer paa noen spm ang konserter. Vennligst bruk smaa bokstaver i svarene.
1. Har du sett dette bandet/artisten paa konsert tidligere? Tror ikke det
huh..!?
2. Hva var den forrige konserten du var paa? Rammstein
3. Ranger Rammstein konserten med ett terningkast 6
Fantastisk!
"""
