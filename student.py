class Student:
    def __init__(self, navn):
        self._antMott = 0
        self._navn = navn
        
    def registrer(self):
        self._antMott += 1
        
    def hentOppmote(self):
        return self._antMott
        
