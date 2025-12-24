class Light:
    def __init__(self, location):
        self.location = location
        self.__is_on = False
        
    
    def turn_on(self):
        self.__is_on = True
        print(f"lamp of {self.location} turn on")
    
    
    def turn_off(self):
        self.__is_on = False
        print(f"lamp of {self.location} turn off")
        
    def status(self):
        if self.__is_on:
            print(f"the lamp of {self.location} is on")
        else:
            print(f"the lamp of {self.location} is off")
            
        
x = Light("hall")

x.turn_on()

x.turn_off()

x.status()



