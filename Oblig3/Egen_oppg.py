"""
IN1000 - Obligatorisk innlevering 3

Oppgave 5: Egen oppgave

5 deltakere til et middagsselskap har ulike allergier.
Lag et program som kan skrive ut allergiene til hver deltaker.
Skriv deretter ut hvilke matvarer man burde unngaa i selskapet.
"""

Deltakere = {"Alf ": ["Gluten", "Tomater"],
             "Kari": ["Lok", "Skalldyr", "Gluten"],
             "Per ": [],
             "Knut": ["Laktose"],
             "Siv ": ["Gluten", "Laktose"]}

Allergier = []
for key, value in Deltakere.items():
    print("%s sine allergier: " %key, value)
    Allergier.extend(value)     # Extend, saa vi bare faar en liste!

print("--"*30)

Allergier.sort()
print("Alle allergiene til gjestene: ", Allergier)

"""
Lager en for-lokke for aa fjerne duplikater.
Lager en ny tom liste mat, der vi appender hver nye allergi som ikke allerede
finnes i listen.
"""
Mat  = []
for word in Allergier:
    if word not in Mat:
        Mat.append(word)

print("Mattyper best aa unngaa:      ", Mat)


""" Sample run
Alf  sine allergier:  ['Gluten', 'Tomater']
Kari sine allergier:  ['Lok', 'Skalldyr', 'Gluten']
Per  sine allergier:  []
Knut sine allergier:  ['Laktose']
Siv  sine allergier:  ['Gluten', 'Laktose']
Alle allergiene til gjestene:  ['Gluten', 'Gluten', 'Gluten', 'Laktose', 'Laktose', 'Lok', 'Skalldyr', 'Tomater']
Mattyper best aa unngaa:       ['Gluten', 'Laktose', 'Lok', 'Skalldyr', 'Tomater']
"""
