"""
Obligatorisk innlevering 1

Progmmet beslutninger.py inneholder en if test med if, elif og else tester.
I tillegg til bruk av input() og print()
"""

brus = input("Kunne du tenke deg en brus? Vennsligst svar ja eller nei. ")

if brus == "ja":
    print("Her har du en brus!")
elif brus == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")


""" Sample run
(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000>python beslutninger.py
Kunne du tenke deg en brus? Vennsligst svar ja eller nei. ja
Her har du en brus!

(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000>python beslutninger.py
Kunne du tenke deg en brus? Vennsligst svar ja eller nei. nei
Den er grei.

(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000>python beslutninger.py
Kunne du tenke deg en brus? Vennsligst svar ja eller nei. hmm
Det forstod jeg ikke helt.
"""
