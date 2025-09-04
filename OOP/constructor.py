class Hero:
    # Static variable 
    jumlah = 0
    def __init__(self, nameHero, Health, Attack, strengh):
        self.nameHero = nameHero
        self.healthhero = Health
        self.attackhero = Attack
        self.strengHero = strengh
        Hero.jumlah += 1




hero1 = Hero("Fanny", 100, 20, 30)
print(Hero.jumlah)
hero2 = Hero("Ripper", 100, 15, 40)
print(Hero.jumlah)


print("\n")
print("-"*10)
print("\n")

print(hero1.__dict__)
print("hero name :", hero1.nameHero)
print("damage attack : ", hero1.attackhero)
print("hero health : ", hero1.healthhero)
print("hero strengh : ", hero1.strengHero)
print("\n")
print("-"*10)
print("\n")
print("hero name :", hero2.nameHero)
print("damage attack : ", hero2.attackhero)
print("hero health : ", hero2.healthhero)
print("hero strengh : ", hero2.strengHero)
