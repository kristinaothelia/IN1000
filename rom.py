class Rom :

    # konstruktøren henter verdier til alle instansvariablene i det nye objektet
    # fra parametrene:
    def __init__(self, nr, navn, type, ant) :
        self._nr = nr
        self._navn = navn
        self._type = type
        self._ant = ant

    # metoden returnerer True eller False avhengig av om påstanden stemmer:
    # rommet har minst så mange plasser som du ber om, og riktig op.sys.
    def passer(self,antP,opsys):
        return (self._ant >= antP and self._type == opsys)
    
    #metoden skriver ut en formattert linje med data i objektet self, på terminal
    def skrivLinje(self) :
        print ("%d %-15s %-15s %d" % (self._nr, self._navn,
                self._type, self._ant))
