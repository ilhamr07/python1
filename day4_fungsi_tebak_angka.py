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

def tebak_angka(tebakan,angka_random):
    if tebakan > angka_random:
        print("Nilai Terlalu besar")
        return False
    elif tebakan < angka_random:
        print("Nilai Terlalu kecil")
        return False
    else :
        print("Anda Benar")
        return True


def main_game():

    random_number = random.randint(1,10)
    while True :