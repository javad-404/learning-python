class Car:
    def __init__(self, model, color):
        self.model= model
        self.color = color
        
        
    def boogh (self):
            print(f"beep beep man model {self.model} hastam va rangam hast {self.color}")

car_1 = Car("pride", "abi")
car_1.boogh()


car_2 = Car("benz", "zard")
car_2.boogh()



        