class Hero :
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    
    def info(self):
        print("{}, {}".format(self.name, self.health))

#inheritance class from Hero Class
class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name,100)
        super().info()

#inheritance class from Hero Class
class Hero_agility(Hero):
    def __init__(self, name):
        super().__init__(name,300)
        super().info()

line = Hero("linea", 400)
axa= Hero_agility("axa")
baxia = Hero_strength("baxia")
