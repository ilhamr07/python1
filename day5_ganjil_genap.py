def genap(a, b):
    print("Genap :",end="")
    for i in range(a,b+1):
        if i%2==0:
            print(i,end=", ")

def ganjil(a, b):
    print("Ganjil :",end="")
    for i in range(a,b+1):
        if i%2==1:
            print(i,end=", ")


awal = int(input("angka awal:"))
akhir = int(input("angka akhir:"))
ganjil(awal,akhir)
print()
genap(awal,akhir)
    
