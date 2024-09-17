from abc import ABC, abstractmethod

class Telefon(ABC):
    def __init__(self, brendi, modeli, id, narxi, tezkor_xotira_hajmi):
        self.__id = id
        self._narxi = narxi
        self.tezkor_xotira_hajmi = tezkor_xotira_hajmi
        self.brendi = brendi
        self.modeli = modeli

    @abstractmethod
    def id_sini_korish(self):
        pass

    @abstractmethod
    def narx_qoyish(self, narx):
        pass

    @abstractmethod
    def narxini_korish(self):
        pass

class IPhone(Telefon):
    def id_sini_korish(self):
        return self.__id

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi

class Samsung(Telefon):
    def id_sini_korish(self):
        return self.__id

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi

telefon1 = Samsung("Samsung", "Galaxy A03S", 1, 350, 4)
telefon2 = IPhone("Apple", "iPhone XV ProMax", 2, 1200, 6)

import json

def save_to_file(telefons, filename='telefons.json'):
    with open(filename, 'w') as file:
        json.dump([{'brendi': t.brendi, 'modeli': t.modeli, 'id': t.id_sini_korish(), 'narxi': t.narxini_korish(), 'tezkor_xotira_hajmi': t.tezkor_xotira_hajmi} for t in telefons], file)

def load_from_file(filename='telefons.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Samsung(t['brendi'], t['modeli'], t['id'], t['narxi'], t['tezkor_xotira_hajmi']) if t['brendi'] == "Samsung" else IPhone(t['brendi'], t['modeli'], t['id'], t['narxi'], t['tezkor_xotira_hajmi']) for t in data]
    except FileNotFoundError:
        return []

def main():
    telefons = load_from_file()
    
    while True:
        print("0. Chiqish")
        print("1. Telefon qo'shish")
        print("2. Telefonlarni ko'rish")
        print("3. Telefon ustida amallar")
        tanlov = int(input("Tanlovingizni kiriting: "))
        
        if tanlov == 0:
            save_to_file(telefons)
            break
        elif tanlov == 1:
            brendi = input("Brendi: ")
            modeli = input("Modeli: ")
            id = int(input("ID: "))
            narxi = float(input("Narxi: "))
            tezkor_xotira_hajmi = int(input("Tezkor xotira hajmi (GB): "))
            if brendi.lower() == "samsung":
                telefons.append(Samsung(brendi, modeli, id, narxi, tezkor_xotira_hajmi))
            elif brendi.lower() == "iphone":
                telefons.append(IPhone(brendi, modeli, id, narxi, tezkor_xotira_hajmi))
        elif tanlov == 2:
            for t in telefons:
                print(f"Brendi: {t.brendi}, Modeli: {t.modeli}, ID: {t.id_sini_korish()}, Narxi: {t.narxini_korish()}, Tezkor xotira: {t.tezkor_xotira_hajmi}GB")
        elif tanlov == 3:
            id = int(input("ID si bo'yicha telefonni tanlang: "))
            telefon = next((t for t in telefons if t.id_sini_korish() == id), None)
            if telefon:
                print(f"ID: {telefon.id_sini_korish()}")
                narx = float(input("Yangi narx qo'yish: "))
                telefon.narx_qoyish(narx)
                print(f"Yangi narxi: {telefon.narxini_korish()}")
            else:
                print("Telefon topilmadi!")

if __name__ == "__main__":
    main()