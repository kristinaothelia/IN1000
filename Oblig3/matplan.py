"""
IN1000 - Obligatorisk innlevering 3

Oppgave 4: Matplan
Vi definerer en ordbok med navn og meny, i form av en liste.
Videre spor programmet brukeren om aa skrive inn et navn, dette navnet
blir sjekket mot navnene i ordboken. Dersom navnet er der blir menyen skrevet
ut, hvis ikke kommer det en feilmelding.
"""

Beboere_mat = {"Kari": ["Brod", "Egg", "Polser"],
               "Kurt": ["Omelett", "Salat", "Pizza"],
               "Kris": ["Brod", "Omelett", "Taco"]}

def Beboer(Beboer):

    if Beboer in Beboere_mat:
        print(Beboere_mat[Beboer])
    else:
        print("Denne navnet kjenner vi ikke!")

Beboer(Beboer=input("Beboers navn?: (Eks Kari, med stor forbokstav) "))

""" 3)

a)
Brukernavn på alle IN1000 studentene

For brukernavn paa alle IN1000 elevene ville jeg brukt en liste.
Fordi det er en samling med "like" verdier.

b)
Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000

For brukernavn og antall poeng ville jeg brukt en ordbok.
Da kan man enkelt legge inn brukernavn med tilhorende poengverdi. Og man kan
enkelt faa ut en bestemt elevs poengverdi.

c)
Alle vinnere i Lotto siste år (kun navn)

Her ville jeg bare brukt en liste.
Man kan eks enkelt legge til en ny verdi for en ny vinner. Som 1) er det
en enkel metode aa samle like verdier i.

d)
All mat noen gjest i et selskap er allergisk mot (for å planlegge menyen)

Her ville jeg brukt en mengde. En ordbok med lister inni.
Man bruker gjestens navn som Key, og bruker lister som rmser opp mat til hver
gjest. Da kan man enkelt skrive ut allergiene til hver gjest.
Evt kan en allergi vere Key, og hver allergi har en lite med navn.
"""
