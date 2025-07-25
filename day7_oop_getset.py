class Hero:

    def __init__(self, name, health, attackPower, defend):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
        self.__defend = defend

    
    @property
    def info(self):
        return "nickname :{} \n" \
        "\thealth :{} \n" \
        "\tattackPower :{} \n" \
        "\tDefend :{}".format(self.__name,self.__health,self.__attackPower,self.__defend)



    def attack(self, lawan):
        print(f"{self.__name} melakukan penyerangan ke {lawan.__name} dengan attack : {self.__attackPower}")
        lawan.__health = lawan.__health - self.__attackPower
        print(f"Darah {lawan.__name} saat ini {lawan.__health}")
        print(f"{lawan.__name} ayooo serang balik !!")
        print("")
        lawan.serangBalik(self)

    def serangBalik(self,lawan):
        print(f"{self.name} menyerang {lawan.name} dengan attack : {self.__attackPower}")
        lawan.__health = lawan.__health - self.__attackPower 
        print(f"darah lapu-lapu saat ini : {lawan.__health}")
        print()
    
    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

   

lapuLapu = Hero("lapuLapu",100,10,20)
vexana = Hero("vexana",80,30,15)

print(lapuLapu.info)
print(vexana.info)

lapuLapu.attack(vexana)
lapuLapu.attack(vexana)
vexana.attack(lapuLapu)


print(lapuLapu.info)
print(vexana.info)
