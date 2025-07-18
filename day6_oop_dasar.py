class Hero:
    def __init__(self, name, health, power, defend):
        self.name = name
        self.health=health
        self.power=power
        self.defend= defend
    
    def serang(self, lawan):
        print(self.name,"Menyerang", lawan.name, "dengan attack =",self.power)
        lawan.diserang(self)

    def diserang(self,lawan):
        darah_diserang= self.health-lawan.power
        print(f"Health",self.name ," saat ini : ",darah_diserang)
        print(self.name," menyerang balik ",lawan.name,"dengan attack:",self.power )
        darah_penyerang = lawan.health - self.power
        print(f"health {lawan.name} saat ini :{darah_penyerang}")


hero1 = Hero("badang",1400,200,80)
hero2 = Hero("Lapu-Lapu",1400,250,10)

hero1.serang(hero2)
print()
hero1.serang(hero2)
print()
hero2.serang(hero1)
print()

print(hero1.__dict__)
print(hero2.__dict__)