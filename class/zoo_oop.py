class Animal:
    zoo_name = "haji zoo"
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        
    def __str__(self):
        return f"name:{self.name}\nspecies: {self.species}\nage: {self.age}\nsound : {self.sound}"
    
    def make_sound(self):
        print(f"{self.sound}")
    def info(self):
        print(self)

class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
        
    def make_sound(self):
        
        def make_sound(self):
            print(f"Parande mige: {self.sound}")
                  
    
        
t1 = Animal("lion", "pestandar", 10 , "goooog")
t2 = Bird("kalag", "parandeh", 20, "gar gar", 2)

t2.info()


        
        
