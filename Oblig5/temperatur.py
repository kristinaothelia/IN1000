"""
IN1000 - Obligatorisk innlevering 5

Oppgave 2: Temperatur

Dette programmet leser inn en fil med temperaturer, og legger temperaturene
inn i en liste. Deretter lager vi en liste med navn paa alle manedene, og
kobler sammen temp og mnd i en for-lokke.
I lokken summerer vi ogsaa sammen temperaturen for alle manedene, og
regner ut et gj.snitt for aaret.
"""

import numpy as np

myfile = open("temperatur.txt")
temps = []

for line in myfile:

    temp = int(line)
    temps.append(temp)

def Temperature(temps):

    temp_average = 0
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

    for i in range(12):
        month = months[i]
        temp  = temps[i]
        temp_average += temp

        print("The average temperature for %-9s is %3g degrees C" %(month, temp))

    #average_yr = np.mean(temps)
    #print("The average temperature for the year is ", average_yr)
    average_yr = temp_average/12
    print()
    print("The average temperature for the year is %g degrees C" % average_yr)

Temperature(temps)
