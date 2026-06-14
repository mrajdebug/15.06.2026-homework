import os
os.system ('cls')

class Talaba:
    def __init__(self, n: str, a: int):
        self.name  = n
        self.age = a

class Kurs:
    def __init__(self, k_n: str, k_t: str):
        self.kurs_nomi = k_n
        self.kurs_teacher = k_t
        self.talabalar_soni = 0
        self.talabalar = []

    def add_new_student(self, n):
        self.talabalar.append(n)
        self.talabalar_soni += 1
        print(f"{n.name} - talaba kursga qo`shildi!!!")

    def delete_new_student(self, talaba):
        for student in self.talabalar:
            if student.name == talaba:
                self.talabalar.remove(student)
                self.talabalar_soni -= 1
                print(f"{talaba} - talaba kursdan o`chirildi!!!")
                return
            
            
        print(f"{talaba} - talaba kursdan topilmadi!!!")

    def info_kurs(self):
        print(f"Jami talabalar: {self.talabalar_soni} ta")
        print("Kursdagilar: ")
        for sa in self.talabalar:
            print(f"{sa.name} - {sa.age}")
        print("-" * 30)

k = Kurs(
    input("Kurs nomi >>> "),
    input("Kursning ustozi >>> ")
)

print("\n10 ta talaba nomini kiriting: >>> ")
for n in range(10):
    ism = input(f"{n+1} - talabaning nomi >>> ")
    yosh = int(input(f"{n+1} - talabaning yoshi >>> "))
    yangi_talaba = Talaba(ism, yosh)

    k.add_new_student(yangi_talaba)

k.info_kurs()

print("\nQaysi talabani o`chirmoqchisiz? >>> ")
ochirish = input("Talaba ismi? >>> ")
k.delete_new_student(ochirish)

k.info_kurs()


