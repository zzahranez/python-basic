class Hero:
    jumlah_hero = 0
    def __init__(self, HeroName, HeroHealth, HeroAttack, HeroStrengh):
        self.name = HeroName
        self.health = HeroHealth
        self.attack = HeroAttack
        self.strengh = HeroStrengh
        Hero.jumlah_hero += 1
    
    def whoIsHero(self):
        print("My name is " + self.name)
        print("I can up myhealth you are will hard to kill me")

    def useSkillUpHealth(self, upHealth):
        self.health += upHealth

    def basicAttack(self, targetHero):
        targetHero.health -= self.attack
        print(f"{self.name} menyerang {targetHero.name} sebesar {self.attack} damage !")
        print(f"{targetHero.name} sisa health : {targetHero.health}")
    
hero1 = Hero("Rafeala ", 100, 5, 10)
hero2 = Hero("Alucard", 100, 10, 5)

print("\n")
print("-"*20)

print("=====> Early playing game <======")
print("Hero name : ", hero1.name)
print("Hero health : ", hero1.health)
print("Hero attack : ", hero1.attack)
print("Hero strengh : ", hero1.strengh)

print("\n")
print("-"*20)

hero1.whoIsHero()
hero1.useSkillUpHealth(20)
print("Now Health : ", hero1.health)

hero2.whoIsHero()
print("Now Health : ", hero2.health)

print("-"*20)
print("\n")
print("-"*20)
print("Tempur boss")
print("-"*20)
for i in range(20):
    hero2.basicAttack(hero1)
    hero1.basicAttack(hero2)
    # setiap 5 serangan hero2
    if i % 5 == 0:
        hero1.useSkillUpHealth(20)  # misal nambah 20 health
        print(f"{hero2.name} menggunakan skill UpHealth! Sisa health sekarang: {hero2.health}")
    
    print(f"Serangan ke-{i}")
    print(f"Sisa health {hero1.name}: {hero1.health}")
    print(f"Sisa health {hero2.name}: {hero2.health}\n")
    
    # cek kalau salah satu hero mati
    if hero1.health <= 0 or hero2.health <= 0:
        print("Battle selesai!")
        break

print("====> SISA HEALTH <====")
if hero2.health <= 0 or hero1.health <= 0:
    print(f"{hero2.name} sudah kalah atau sisa health: {hero2.health}")
    print(f"{hero1.name} sudah kalah atau sisa health: {hero1.health}")
else:
    print(f"Sisa health {hero2.name} : {hero2.health}")
    print(f"Sisa health {hero1.name} : {hero1.health}")
 




        