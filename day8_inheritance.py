#super Class
class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

#inheritance class from Hero Class
class Hero_strength(Hero):
    pass

#inheritance class from Hero Class
class Hero_agility(Hero):
    pass

lina=Hero("Line", 100)
axa= Hero_agility("axa", 70)
baxia = Hero_strength("baxia",100)

print(lina.name)
print(axa.name)
print(baxia.name)