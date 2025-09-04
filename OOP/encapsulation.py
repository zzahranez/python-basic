from helper import HeroDescription, Ngenter, NgenterDua

print("----> ENCAPSULATION <----")
print("-"*20)


class Hero:

    def __init__(self, name, health, attackPower, Armor):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
        self.__armor = Armor

    # Setter
    def setName(self, name):
        self.__name = name

    def setHealth(self, health):
        self.__health = health

    def setAttackPower(self, attackPower):
        self.__attackPower = attackPower
    def setArmor(self, armor):
        self.__armor = armor

    # Getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def getAttackPower(self):
        return self.__attackPower

    def getArmor(self):
        return self.__armor

timemaster = Hero("TimeMaster",100, 15,5)


HeroDescription(timemaster.getName(), timemaster.getHealth(), timemaster.getAttackPower(), timemaster.getArmor())
Ngenter()

timemaster.setName("Thamuz")
timemaster.setHealth(120)
timemaster.setAttackPower(20)
timemaster.setArmor(15)
HeroDescription(timemaster.getName(), timemaster.getHealth(), timemaster.getAttackPower(), timemaster.getArmor())
