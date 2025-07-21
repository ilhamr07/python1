class A:
    def show(self):
        print("ini adalah show A")

class B:
    def show(self):
        print("ini adlaah show B")        

class C(B,A):
    
    #def show(self):
        #print("ini adlaah show C") 
        pass

objek = C()

objek.show()

help(objek)
