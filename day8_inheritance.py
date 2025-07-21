class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

#inheritance from Hero Class
class Hero_strength(Hero):
    pass

class Hero_agility(Hero):
    pass

lina=Hero("Line", 100)
axa= Hero_agility("axa", 70)
baxia = Hero_strength("baxia",100)

print(lina.name)
print(axa.name)
print(baxia.name)