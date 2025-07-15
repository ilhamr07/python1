import random

#membuat angka random
random_number = random.randint(1,10)

kesempatan = False

while kesempatan == False:
    tebakan = int(input(f"tebak angka (1-10) :"))
    if tebakan > random_number :
        print("Angka Terlalu besarr!!")
    elif tebakan < random_number :
        print('Angka Terlalu Kecil!')
    else :
        print('Selamat Jawaban anda Benar')
        exit()
    
    # kesempatan +=1

