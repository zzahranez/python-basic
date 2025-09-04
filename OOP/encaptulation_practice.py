from helper import HeroDescription, Ngenter, NgenterDua

print("--> ENCAPTULATION PRACTICE <--")
Ngenter()

class Hero:
    __jumlah = 0
    
    def __init__(self, name, health, attPower, armor):
      self.__name = name
      self.__healthStandard = health
      self.__attPowerStandard = attPower
      self.__armorStandard = armor
      self.__level = 1
      self.__exp = 0

      self.__healthMax = self.__healthStandard * self.__level
      self.__attPower = self.__attPowerStandard * self.__level
      self.__armor = self.__armorStandard * self.__level
      self.__expthresold = 100

    #   Health hero
      self.__health = self.__healthMax
      Hero.__jumlah += 1

    @property
    def info(self):
       return "{} \n\tHealth : {}/{}\n\tAttackPower : {}\n\tArmor : {}\n\tLevel : {}\n\tExp : {}".format(self.__name, self.__health, self.__healthMax, self.__attPower, self.__armor, self.__level, self.__exp)
    @property
    def gainExp(self):
       pass
    @gainExp.setter
    def gainExp(self, addExp):
       self.__exp += addExp
       if (self.__exp >= self.__expthresold):
          print(self.__name, "level up")
          self.__level += 1
          self.__exp -= 100

          self.__healthMax = self.__healthStandard * self.__level
          self.__attPower = self.__attPowerStandard * self.__level
          self.__armor = self.__armorStandard * self.__level
          self.__expthresold += 30
    
    def attack(self, enemies):
     if enemies.__health <= 0:
        print(f"{enemies.__name} sudah mati, tidak bisa diserang lagi.")
        return

     print(f"{self.__name} menyerang {enemies.__name}")
     enemies.__health -= self.__attPower

     if enemies.__health <= 0:
        print(f"{enemies.__name} mati!")
        self.gainExp = 50


    def levelingGoblin(self, goblin):
       for i in range (goblin):
          self.gainExp = 50
          


jack = Hero("Jack", 100,40,3)
goblin = Hero("Goblin", 100,7,10)
orch = Hero("Orch", 100, 5,15)

for i in range(20):
    jack.attack(goblin)
    NgenterDua

for i in range(5):
   jack.attack(orch)
   NgenterDua

print(jack.info)
print(goblin.info)
print(jack.info)

