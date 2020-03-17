from random import randint
from celle  import Celle

class Spillebrett:

    def __init__(self, rader, kolonner):

        self._gen      = 0              # Set the initial generation to 0
        self._rader    = rader
        self._kolonner = kolonner
        self._brett    = [[Celle() for i in range(self._kolonner)] for i in range(self._rader)]
        # https://stackoverflow.com/questions/43166038/how-to-create-a-2d-list-from-a-input-data

        """
        self._brett = []
        for i in range(self._rader):
            self._brett.append([])
            for j in range(self._kolonner):
                self._brett[i].append(Celle())
        """
        self._generer()                 # Generate the first board


    def _generer(self):

        for i in self._brett:
            for j in i:
                liv = randint(0, 2)
                # Set "dead" or "alive" with settDoed or settLevende from Celle
                if liv < 2:
                    j.settDoed()
                else:
                    j.settLevende()

    def tegnBrett(self):
        """
        Nested for-loop to print each elemt on the board
        """
        print("\n\n\n")         # Empty the game board/terminal

        for i in self._brett:
            print("")           # new line in game board
            for j in i:
                print(j.hentStatusTegn(), end="")

    def oppdatering(self):
        """
        The status of the cell is determined by the following game rules:

        If the status of the cell is "alive":
        - The cell dies if less than two neighbour-cells are alive (under population)
        - The cell stays alive if there are 2 or 3 alive neighbour-cells
        - With more than 3 alive neighbour-cells, the cell dies (over population)

        If the cell is "dead":
        - The cell is reborn if it got 3 alive neighbours
        """
        leve = []
        dode = []

        for i in range(len(self._brett)):
            for j in range(len(self._brett[i])):

                # Find neighbours
                naboer  = self.finnNabo(i, j)
                levende = []

                # Find how many neighbours are alive. Append to list 'levende'
                for k in naboer:
                    if k.erLevende():
                        levende.append(k)

                # If 2 or 3 neighbours --> The cell stays alive
                if self._brett[i][j].erLevende() and len(levende) in range(2, 4):
                    leve.append(self._brett[i][j])
                # The cell is reborn with 3 alive neighbours
                elif not self._brett[i][j].erLevende() and len(levende) == 3:
                    leve.append(self._brett[i][j])
                # The cell dies if we have less than 2 or more than 4 neighbour cells are alive
                else:
                    dode.append(self._brett[i][j])

        for set_status in dode:
            set_status.settDoed()

        for set_status in leve:
            set_status.settLevende()

        self._gen += 1

    def finnAntallLevende(self):
        """
        A function that counts the number of alive cells on the board.
        """
        antall_levende = 0  # Teller

        for i in range(len(self._brett)):
            for j in range(len(self._brett[i])):

                if self._brett[i][j].erLevende():

                    antall_levende += 1

        return antall_levende


    def finnNabo(self, rad, kolonne):
        """
        Find the neighbour of a random cell. Koordinates --> (rad, kolonne)
        We have to use the board; _brett

        Range: (Piazza tips)
        -1 --> We move to the index one spot back in the board (x_{n-1})
         0 --> The index for the 'home'-cell (x_n)
         1 --> We move to the index one space further in the board (x_{n+1})
        """
        naboer = []

        for i in range(-1, 2):
            for j in range(-1, 2):

                nabo_rad = rad + i          # Move one index, for rows
                nabo_kol = kolonne + j      # Move one index, for columns

                Nabo = True

                # We have to make sure that a neighbour cell do not get the
                # same index as the 'home'-cell. (When ex. nabo_rad = rad + 0)
                if nabo_rad == rad and nabo_kol == kolonne:
                    Nabo = False

                # We do not want to append a neighbour outside the board
                # This is when the neighbour < 0 or > -1 (last object in list)

                # Check for each row
                if nabo_rad < 0 or nabo_rad >= self._rader:
                    Nabo = False

                # Check for each column
                if nabo_kol < 0 or nabo_kol >= self._kolonner:
                    Nabo = False

                if Nabo:
                    # Append when the index is a neighbour
                    naboer.append(self._brett[nabo_rad][nabo_kol])

        return naboer
