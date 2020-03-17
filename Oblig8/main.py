"""
IN1000 - Oblig 8: Conway’s Game of life
"""

from spillebrett import Spillebrett

def main():
    print("Game of life")
    rader    = int(input("Antall rader:    "))
    kolonner = int(input("Antall kolonner: "))

    # Generate the board and plot generation 'zero'
    Game = Spillebrett(rader, kolonner)
    Game.tegnBrett()
    print("\n\nGenereasjon: %g. Antall levende celler: %g" %(Game._gen, Game.finnAntallLevende()))

    print("--"*41)
    Next = input("Press enter to continue to the next generation, or 'q' and enter to quit the game. ")

    # Keep opdting the game board until the user ends the game
    while Next != "q":
        Game.oppdatering()
        Game.tegnBrett()
        print("\n\nGenereasjon: %g. Antall levende celler: %g" %(Game._gen, Game.finnAntallLevende()))

        print("--"*41)
        Next = input("\nPress enter to continue to the next generation, or 'q' and enter to quit the game. ")

main()
