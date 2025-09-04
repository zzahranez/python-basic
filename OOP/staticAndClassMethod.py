from helper import HeroDescription, Ngenter, NgenterDua

print("--> STATIC METHOD AND CLASS METHOD <--")
print("\n")

class Gebetan:
    __jumlah = 0
    def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Gebetan.__jumlah += 1

    @staticmethod
    def getJumlah():
       return Gebetan.__jumlah
    @classmethod
    def getJumlahObj(cls):
       return cls.__jumlah

liya = Gebetan("Liya", 19)
print(Gebetan.getJumlah())
dini = Gebetan("Dini", 20)
print(Gebetan.getJumlahObj())
