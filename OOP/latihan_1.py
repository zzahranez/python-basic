from helper import HeroDescription, Ngenter, NgenterDua

class Hero:
    def __init__(self, name, health, attack, armor, lifesteal):
      self.name = name
      self.health = health
      self.attack = attack
      self.armor = armor
      self.lifesteal = lifesteal 
      self.attack_counter = 0 

    def serang(self, enemies):
        print(self.name , "Menyerang", enemies.name)
        enemies.diserang(self, self.attack)

        if self.lifesteal:
            self.attack_counter += 1
            if self.attack_counter % 5 == 0: 
                self.health += 2
                print(f"✨ {self.name} lifesteal +2 HP! (Total HP: {self.health})")


    def diserang(self, enemies, damage):
        print(self.name , "Diserang", enemies.name)
        damageDiterima = damage / self.armor
        self.health -= damageDiterima

sniper = Hero("Sniper", 100, 40, 5, lifesteal=True)
HeroDescription(sniper.name,sniper.health,sniper.attack,sniper.armor)
Ngenter()

alucard = Hero("Alucard", 100,15, 20, lifesteal=False)
HeroDescription(alucard.name, alucard.health, sniper.attack, sniper.armor)
Ngenter()

for i in range(7):
    print(f"Basic Attack ke -{i}")
    print("\n")
    sniper.serang(alucard)
    print("-"*20)
    alucard.serang(sniper)
    print("-"*20)
    print("Sniper Health : ",sniper.health)
    print("Alucard Health : ",alucard.health)

Ngenter()
if sniper.health < alucard.health:
   print("Sniper kalah")
else:
   print("Alucard kalah")