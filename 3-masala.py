import os
os.system ("cls")

class String:
    def __init__(self, matn: str):
        self.matn = matn

        self.kichik_alifbo = "abcdefghijklmnopqrstuvwxyz"
        self.katta_alifbo  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def to_lower(self):
        natija = ""

        for harf in self.matn:
            if harf in self.katta_alifbo:
                indeks = self.katta_alifbo.index(harf)
                natija += self.kichik_alifbo[indeks]
            else:
                natija += harf

        return natija
    
    def to_upper(self):
        natija = ""

        for harf in self.matn:
            if harf in self.kichik_alifbo:
                indeks = self.kichik_alifbo.index(harf)
                natija += self.katta_alifbo[indeks]
            else:
                natija += harf
        
        return natija
    
    def is_lower(self):
        for harf in self.matn:
            if harf in self.katta_alifbo:
                return False
            return True
        
    def is_upper(self):
        for harf in self.matn:
            if harf in self.kichik_alifbo:
                return False
            return True
        
s = String("Namuna")
print(s.is_lower())
print(s.to_lower())
print(s.is_upper())
print(s.to_upper())
