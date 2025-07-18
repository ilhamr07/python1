class Hero:
    def __init__(self, name, health, power, defend):
        self.name = name
        self.health=health
        self.power=power
        self.defend= defend
    
    def serang(self):
        print(self.name,"Menyerang")


hero1 = Hero("badang",1400,200,80)

hero1.serang()

print(hero1.__dict__)