class Car:
    def __init__(self,brand,colour):
        self.brand = brand
        self.colour = colour
        
    def start(self):
        print(f"{self.colour} {self.brand} is starting...")
        
car1 = Car("Defender","Red")
car2 = Car("Honda","Blue")

car1.start()    
car2.start() 



# Instance vs Class Variables
class Employee:
    company = "TechCorp"  # Class variable
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Instance variables
        
e1 = Employee("John", 50000)
e2 = Employee("Emma", 60000)

