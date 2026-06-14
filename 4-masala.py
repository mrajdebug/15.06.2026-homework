import os
os.system ("cls")

class Taqvim:
    def __init__(self, yil: int):
        self.yil = yil

    def hijriyga(self):
        natija = (self.yil - 622) * 1.032
        return int(natija) 
    
    def grigoriyanga(self):
        natija = (self.yil/1.032) + 622
        return int(natija)
    
    def kabisami(self):
        if self.yil % 400 == 0:
            return True
        elif self.yil % 100 == 0:
            return False
        elif self.yil % 4 == 0:
            return True
        else:
            return False
        
t1 = Taqvim(2026)
print(f"2026-yil Hijriy taqvimda: {t1.hijriyga()}") 

t2 = Taqvim(1448)
print(f"Hijriy 1448-yil: {t2.grigoriyanga()}")

t4 = Taqvim(2026)
print(f"2026-yil kabisa yili: {t4.kabisami()}") 

