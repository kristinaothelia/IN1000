from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn   = listenavn

    def lesFraFil(self, filnavn):
        """
        Metoden aapner den oppgitte filen, og leser inn data om sanger
        – en linje per sang, paa formatet: tittel;artist
        """
        Fil = open(filnavn, 'r')

        for lines in Fil:
            data   = lines.strip().split(';') # Splitter tittel og artist
            tittel = data[0]
            artist = data[1]

            sang_  = Sang(tittel, artist)
            self._sanger.append(sang_)

        Fil.close()

    def leggTilSang(self, nySang):
        """
        'nySang' er det nye objektet som skal legges til i spillelisten.
        """
        self._sanger.append(nySang)

    def fjernSang(self, sang_):
        """ Fjern sangen fra spillelisten """
        t, a = sang_.Return_tittel_artist()

        if sang_ in self._sanger:
            print('Fjernet sangen "%s" av %s fra spillelisten' % (t,a))
            self._sanger.remove(sang_)

    def spillSang(self, sang_):
        """ Spill av sangen """
        sang_.spill()

    def spillAlle(self):
        """ Spiller alle sangene i spillelisten """
        print(self._navn)
        for i in self._sanger:
            i.spill()

    def finnSang(self, tittel):
        """
        Leter gjennom listen av sanger etter en sang med den oppgitte tittelen
        og returnerer den forste den finner.
        Finnes ikke tittelen i spillelisten returneres None.
        """
        for i in self._sanger:
            # Bruker sjekkTittel fra sang klassen
            if i.sjekkTittel(tittel):
                return i
        else:
            return None

    def hentArtistUtvalg(self, artistnavn):
        """
        Metoden gaar gjennom alle sanger i spillelisten og tar vare paa de som
        har en eller flere navn fra parameteren artistnavn i navnet paa
        artisten. Disse returneres i en liste med sanger.
        """
        utvalg = []

        for i in self._sanger:
            # Bruker sjekkArtist fra sang klassen
            if i.sjekkArtist(artistnavn):
                utvalg.append(i)

        return utvalg
