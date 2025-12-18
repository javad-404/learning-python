class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def attack(self):
        print("Heroes fight differently")
        
        
class Warrior(Hero):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength
    def attack(self):
        print(f"Attacking with Sword! Damage: {self.strength}")
        
        
class Mage(Hero):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana
    def attack(self):
        print(f"Casting Fireball! Cost: {self.mana} mana")
        
        
w1 = Warrior("Aragorn", 100, 50) 
m1 = Mage("Gandalf", 80, 200)       
team = [w1, m1]
for A in team:
    A.attack()
    
         
        
    
        
        