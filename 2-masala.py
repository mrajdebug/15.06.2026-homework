import os
os.system ('cls')

from translate import Translator

class Convertor:
    def __init__(self):

        self.ru_tarjimon = Translator(from_lang='ru', to_lang='en')

        self.en_tarjimon = Translator(from_lang='en', to_lang='ru')

    def ru_to_en(self, matn: str):
        return self.ru_tarjimon.translate(matn)
    
    def en_to_ru(self, matn: str):
        return self.en_tarjimon.translate(matn)
    
konvertor = Convertor()
ruscha_matn = "Я купил новый телефон"
ingliz_matn = konvertor.ru_to_en(ruscha_matn)
print(f"{ruscha_matn} -> {ingliz_matn}")

inglizcha_matn = "I bought a new laptop"
rus_matn = konvertor.en_to_ru(inglizcha_matn)
print(f"{inglizcha_matn} -> {rus_matn}")

# import os
# os.system("cls")
# from translate import Translator

# tarjimon = Translator(to_lang='en', from_lang='ru')

# text = input(">>> ")
# res = tarjimon.translate(text)
# print(res)