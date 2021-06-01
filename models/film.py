class Film:

    def __init__(self, titel, duur, knt, MDB_id):
        self.titel= titel
        self._duur=duur 
        self._knt=knt
        self.MDB_id=MDB_id

    
    @property
    def duur (self):
        return self._duur
        
    @duur.setter
    def duur(self,duur):
        if type(duur)==int :
            self._duur=duur
        else :
            raise ValueError

    @property
    def knt (self):
        return self._knt

    @knt.setter
    def knt(self,knt):
        if knt.upper() in ["T","F"]:
            self._knt=knt.upper()
        else :
            raise ValueError

    def __str__(self):
        return f"de titel van deze film is {self.titel} en duurt {self.duur}min"

    def duurtijd (self):
        uren= int(self.duur/60)
        min=int(self.duur%60)
        return f"{uren} h {min} min"
        
             