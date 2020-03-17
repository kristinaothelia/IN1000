"""
IN1000 - Obligatorisk innlevering 5

Oppgave 1: Regnefunksjoner

Programmet inneholder flere smaa funkjsoner som utforer ulike beregninger.
Funksjonene returnerer saa den utregnede verdien.
Det blir brukt assert tester paa enkelte funksjoner for aa teste at de
fungerer som de skal.
"""

def addisjon(a, b):
    return int(a) + int(b)

Add = addisjon(a=5, b=2)
print("Addisjonen ble: ", Add)

def substraksjon(a, b):
    return int(a) - int(b)

# Test at funk. substraksjon fungerer, med assert
assert substraksjon(a=5, b=2)   ==  3.0
assert substraksjon(a=-5, b=-2) == -3.0
assert substraksjon(a=5,  b=-2) ==  7.0

def divisjon(a, b):
    return int(a)/int(b)

# Test at funk. divisjon fungerer, med assert
assert divisjon(a=5, b=2)       == 2.5
assert divisjon(a=-5, b=-2)     == 2.5
assert not divisjon(a=5,  b=-2) == 2.5  # assert == -2.5

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    cm = antallTommer * 2.54
    return cm

tommer = 4
tommer_til_cm = tommerTilCm(antallTommer = tommer)
print("%g tommer tilsvarer %g cm" %(tommer, tommer_til_cm))

def skrivBeregninger():
    a = float(input("Skriv inn et tall: "))
    b = float(input("Skriv inn et tall: "))
    print("Utregninger:")
    print("%g + %g blir %g" %(a, b, addisjon(a, b)))
    print("%g - %g blir %g" %(a, b, substraksjon(a, b)))
    print("%g / %g blir %g" %(a, b, divisjon(a, b)))

    tommer = float(input("Skriv inn antall tommer som skal konverteres til cm: "))
    print("Konvertering:")
    print("%g er %g cm" %(tommer, tommerTilCm(antallTommer=tommer)))

skrivBeregninger()
