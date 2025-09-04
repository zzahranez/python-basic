from helper import HeroDescription, Ngenter, NgenterDua

print("---> GETTER AND SETTER IN PYTHON <---")
NgenterDua()

class Hero:
    
    def __init__(self, name, health, attackPower, armor):
      self.__name = name
      self.__health = health
      self.__attackPower = attackPower
      self.__armor = armor
      self.__info = "name : {} \n health : {}".format(self.__name)

    @property
    def info(self):
       return self.__info
    


sniper = Hero("Sniper", 100, 30, 5)

Ngenter()
print(sniper.info)