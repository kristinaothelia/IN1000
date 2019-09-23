"""
Obligatorisk innlevering 1

Progmmet dato.py utforer en rekke if-tester for aa bestemme hvilken av to input
datoer som skrives inn først
"""


dato1_dag = input("Vennligst oppgi en dato. dd ")
dato1_mnd = input("                      og mm ")
dato2_dag = input("Vennligst oppgi en dato. dd ")
dato2_mnd = input("                      og mm ")

if dato1_mnd < dato2_mnd:           # Tester om dato1_mnd er tidligere enn dato2_mnd
    print("Riktig rekkefolge!")

elif dato1_mnd > dato2_mnd:         # Hvis dato1_mnd kommer etter dato2_mnd
    print("Feil rekkefolge!")

elif dato1_mnd == dato2_mnd:        # Hvis dato1_mnd er lik som dato2_mnd
    if dato1_dag < dato2_dag:       # Tester om dato1_dag kommer for dato2_dag
        print("Riktig rekkefolge!")
    elif dato1_dag == dato2_dag:    # Tester om samme dato
        print("Samme dato!")
    else:                           # Hvis dato2_dag kommer for dato1_dag
        print("Feil rekkefolge!")
