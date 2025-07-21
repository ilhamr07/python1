class Hero:
    
    def __init__(self,name,health):
        self.name = name
        self.health= health
    
    def attack(self):
        print("Serangggggg *_* ")

class Hero_Warior(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        self.attack()
    #override method attack dari class Hero
    def attack(self):
        print(f"{self.name} Menyerang menggunakan pedang X")

class Hero_Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        self.attack()
    #override method attack dari class Hero
    def attack(self):
        print(f"{self.name} Menyerangattack menggunakan Magic ~~x~~")    

class Hero_Archer(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        self.attack()
    #override method attack dari class Hero
    def attack(self):
        print(f"{self.name} Menyerangattack menggunakan Panahh --->--->")

hero1 = Hero_Warior("Nana")
hero2 = Hero_Mage("Baxia")
hero3 = Hero_Archer("Vexana")