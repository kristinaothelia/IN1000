"""
Obligatorisk innlevering 2

Koden konverterer temperatur fra Farenheit til Celcius

Siden input() alltid konverterer inputet til type string/str, saa
endrer vi input typen til float. Da kan input vere tall med og uten desimaler.

Problemet med denne losningen er at programmet prover aa konvertere tekst til
float, noe som ikke gaar. Vil gi en feilmelding!
"""

Temp_F = float(input("Hvor mange grader Farenheit er det? "))

def Fahrenheit():
    """
    %0.2f printer ut et desimaltall med to desimaler
    """
    print("Temperaturen er %0.2f grader F" % Temp_F)


def F_to_C():
    """
    F to C: ((temperatur i fahrenheit) − 32) ∗ 5/9
    """
    FtoC = (Temp_F - 32) * 5/9
    print("Temperaturen er %0.2f  grader C" % FtoC)

""" Kaller funkjonene """

Fahrenheit()
F_to_C()

""" Sample run
(py3) C:\Users\Bruker\Documents\Skole UiO\IN1000\Oblig2>python fahrenheit_celsius.py
Hvor mange grader Farenheit er det? 100
Temperaturen er 100.00 grader F
Temperaturen er 37.78  grader C
"""
