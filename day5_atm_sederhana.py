saldo = 1000000

def cek_saldo():
    print(f"Saldo Anda Saat ini adalah Rp. {saldo}")

def setor(jumlahSetor):
    global saldo
    saldo += jumlahSetor
    return print(f" Saldo anda saat ini adalah :{saldo}" )

def tarik(jumlahTarik):
    global saldo
    saldo -= jumlahTarik
    return print(f" Saldo anda saat ini adalah :{saldo}" )

while True:
    print("===ATM===")
    print("1. Cek Saldo\n2. Setor Tunai\n3. Tarik Tunai\n4. Keluar")
    pilihan = int(input("Pilihan :"))

    if pilihan==1:
        cek_saldo()
    elif pilihan==2:
        a = int(input("Masukan Jumlah : Rp."))
        setor(a)
    elif pilihan==3:
        b = int(input("Masukan Jumlah : Rp."))
        tarik(b)
    elif pilihan ==4:
        break
    else:
        print("Angka yang anda masukan salah! (x_x)")    