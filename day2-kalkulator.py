angka_awal = int(input("Masukan angka pertama : "))
angka_kedua = int(input("Masukan angka kedua : "))
operator = input("Masukan Operator (+ , - , * , / ):")


if operator == "+":
    hitungan = angka_awal + angka_kedua
elif operator =="-":
    hitungan = angka_awal - angka_kedua
elif operator =="*":
    hitungan = angka_awal * angka_kedua
elif operator =="/":
    hitungan = angka_awal / angka_kedua
else :
    print("operator matematika yang ada masukan tidak ada !!")

print(f"Hasil :{hitungan}")