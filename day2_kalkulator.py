from day4_modul_kalkulator import tambah, kurang, kali, bagi

while True: #loop dengan kondisi selalu benarr
    angka_awal = int(input("Masukan angka pertama : "))
    angka_kedua = int(input("Masukan angka kedua : "))
    operator = input("Masukan Operator (+ , - , * , / ):")

    if operator == "+":
        # hitungan = tambah(angka_awal,angka_kedua)
        print(f"hasil : {tambah(angka_awal,angka_kedua)}")
    elif operator =="-":
        # hitungan = angka_awal - angka_kedua
        print(f"hasil : {kurang(angka_awal,angka_kedua)}")
    elif operator =="*":
        # hitungan = angka_awal * angka_kedua
        print(f"hasil : {kali(angka_awal,angka_kedua)}")
    elif operator =="/":
        # hitungan = angka_awal / angka_kedua
        print(f"hasil : {bagi(angka_awal,angka_kedua)}")
    else :
        print("operator matematika yang ada masukan tidak ada !!")
        
    loop= input(f"Hitung Lagi? (y/n): ")
    if loop =="n":
        print("Permainan Berakhirrr")
        break #keluar dari perulangan karna pemain ingin mengakhiri game
    else :
        print("Lanjut Berhitunggg!")
    

