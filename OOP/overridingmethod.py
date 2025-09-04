from helper import HeroDescription, Ngenter, NgenterDua

print("--> OVERIDING METHODS <--")
Ngenter()

class Hero:
    def __init__(self, name, health):
      self.name = name
      self.health = health
    def showinfo(self):
       print(f"Name : {self.name}\nHealth : {self.health}")

class Magician(Hero):
   def __init__(self, name):
     self.name = name
     super().__init__(name, 100)
     super().showinfo()

class Tank(Hero):
   def __init__(self, name):
     self.name = name
     super().__init__(name, 200)
     super().showinfo()


wizard = Magician("Wizard")
Ngenter()
tigreal = Tank("Tigreal")
