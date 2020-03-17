class Sang:

    def __init__(self, tittel, artist):     # Konstruktor

        self._tittel = tittel
        self._artist = artist

    def spill(self):
        """
        "spiller av" musikken for sangen den kalles for
        """
        print('"%-20s", av %s' %(self._tittel, self._artist))

    def Return_tittel_artist(self):
        return self._tittel, self._artist

    def sjekkArtist(self, navn):
        """
        Metoden returnerer True dersom ett eller flere av navnene i strengen
        navn finnes i _artist, ellers False.
        """
        navn        = navn.lower().split()
        artist      = self._artist.lower().split()

        for i in range(len(navn)):
            if navn[i] in artist:
                return True
            

    def sjekkTittel(self, tittel):
        """
        Metoden sjekker om oppgitt tittel er den samme som i instansvariabelen
        og returnerer True ved likhet, ellers False.
        """
        return tittel.lower() == self._tittel.lower()


    def sjekkArtistogTittel(self, artist, tittel):
        """
        Metoden returnerer True dersom både tittelen og artisten stemmer med
        sangens instansvariabler, ellers False.
        """
        # Use "and", not "," --> So that we don't return two return values
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)
