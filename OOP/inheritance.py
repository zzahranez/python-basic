from helper import HeroDescription, NgenterDua, Ngenter

print("--> INHERITANCE <--")
Ngenter()


class Hero:

    def __init__(self, name, health):
      self.__name = name
      self.__health = health

    @property
    def health(self):
       return self.__health
    
    @property
    def name(self):
       return self.__name
    
    @property
    def info(self):
       return "{} \n\t Health : {}".format(self.__name, self.__health)
    
    # Setter
    @health.setter
    def health(self, value):
       self.__health = value

    @name.setter
    def name(self, value):
       self.__name = value

class Tanker(Hero):
    def __init__(self, name, psycaldefence):
      self.name = name
      self.pyscaldefence = psycaldefence
      super().__init__(name, 200)

jack = Hero("Jack", 100)


# Tank
minotaur = Tanker("Minotaur", 100)
print("Name : ", minotaur.name)
print("Health : ",minotaur.health)
print("Psychal defence : ",minotaur.pyscaldefence)

