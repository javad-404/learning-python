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
    def attack(self, enemy):
        enemy.hp -= self.strength
        print(f"{self.name} dare be {enemy.name} hamle mikone!")
        print(f"{self.strength} ta damage khord.")
        print(f"Joon e {enemy.name} shod: {enemy.hp}")
        
        
class Mage(Hero):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana
    def attack(self, enemy):
        enemy.hp -= self.mana
        print(f"{self.name} dare be {enemy.name} hamle mikone!")
        print(f"{self.mana} ta damage khord")
        print(f"joon e {enemy.name} shod : {enemy.hp}")
        
        
w1 = Warrior("Aragorn", 100, 50) 
m1 = Mage("Gandalf", 80, 200)       
team = [w1, m1]
w1.attack(m1)
m1.attack(w1)


    
         
        
    
        
        