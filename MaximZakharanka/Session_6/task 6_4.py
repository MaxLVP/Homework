class Bird():
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk"
    
    def walk(self):
        print(f"{self.name} can walk")
        
    def fly(self):
        print(f"{self.name} can fly")

class FlyingBird(Bird):
    
    ration = "mostly grains"
    
    def __init__(self, name, ration = ration):
        self.name = name
        self.ration = ration
    
    def walk(self):
        return super().walk()
        
    def fly(self):
        return super().fly()
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk and fly"
    
    def eat(self):
        return print(f"It eats {self.ration}")
        
        
class NonFlyingBird(Bird):
    
    ration = "mostly fish"
    
    def __init__(self, name, ration = ration):
        self.name = name
        self.ration = ration
    
    def walk(self):
        return super().walk()
        
    def swim(self):
        print(f"{self.name} can swim")
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk and swim"
    
    def eat(self):
        return print(f"It eats {self.ration}")    
        
class SuperBird(NonFlyingBird, FlyingBird):
    
    ration = "mostly fish"
    
    def __init__(self, name, ration = ration):
        super().__init__(name, ration)
    
    def walk(self):
        super().walk() 
    
    def fly(self):
        super().fly()
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk, swim and fly"
    
    def eat(self):
        super().eat()
