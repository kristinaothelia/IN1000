"""
IN1000 - Obligatorisk innlevering 3

Oppgave 6: Egen oppgave

Skriv et program som lar brukeren legge inn bursdgaer i en ordbok. Skriv saa
ut tid personene har bursdag og alderen deres.
La saa brukeren finne bursdagen til en spesiell person i ordboken.
Skriv ut bursdgaen.
"""
import numpy as np
import time
from datetime import date

def Bursdager():

    print("--"*35)
    print("Skriv inn navn og dato i ordboken. Skriv 'break' naar du vil avslutte.")
    print("--"*35)

    Input_navn = input("Skriv et navn: ")
    Ordbok = {}

    while Input_navn != "break":

        Input_dato = input("Skriv %s sin bursdag: (DD.MM.AAAA) " % Input_navn)
        Ordbok[Input_navn] = Input_dato
        Input_navn = input("Skriv et navn: ")

        if Input_navn == "break":
            break

    return Ordbok

Ordbok = Bursdager()
Month = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

def Print_bursdag(Ordbok):

    for key, value in Ordbok.items():

        x = value.split(".")

        today = date.today()
        today_Y = today.strftime("%Y") # Only want the year
        today_m = today.strftime("%m") # Only want the month
        today_d = today.strftime("%d") # Only want the day

        Age_Y = int(today_Y) - int(x[2])
        Age_m = int(today_m) - int(x[1])
        Age_d = int(today_d) - int(x[0])

        print("--"*35)
        if today_m == x[1]:
            if today_d == x[0]:
                print("%10s blir %s aar i dag! Gratulerer med dagen =)" % (key, Age_Y))
            elif today_d > x[0]:
                print("%10s har bursdag den %s. %s og ble %-4s aar denne maaneden" %(key, x[0], x[1], Age_Y))
            elif today_d < x[0]:
                print("%10s har bursdag den %s. %s og blir %-4s aar denne maaneden" %(key, x[0], x[1], Age_Y))

        elif today_m > x[1]:
            print("%10s har bursdag den %s. %s og ble %-4s aar gammel i aar" %(key, x[0], x[1], Age_Y))

        elif today_m < x[1]:
            print("%10s har bursdag den %s. %s og blir %-4s aar gammel i aar" %(key, x[0], x[1], Age_Y))
        print("--"*35)

Print_bursdag(Ordbok)


def Finn_bursdag(Ordbok):
    print("Navnene i ordboken er: ")
    for key, value in Ordbok.items():
        print(key)

    Finn_b = input("Hvem vil du finne bursdagen til? ")

    x = value.split(".")

    x[1] = int(x[1])
    for i in range(1, len(Month)+1):
        if x[1] == i:
            x[1] = Month[i-1]  # Pga indexeringen
            break

    for key, value in Ordbok.items():
        if Finn_b == key:
            print("%s sin bursdag er den %s.%s.%s" %(key, x[0], x[1], x[2]))
        else:
            print("Dette navnet er ikke i ordboken.")
            Finn_b = input("Skriv et nytt navn: Eller skriv break. ")
            if Finn_b == "break":
                break

Finn_bursdag(Ordbok)
