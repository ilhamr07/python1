class Hero:
    def __init__(self, name, health, power, defend):
        self.name = name
        self.health=health
        self.power=power
        self.defend= defend

hero1 = Hero("badang",1400,200,80)

print(hero1.__dict__)