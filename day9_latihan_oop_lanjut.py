import random

# Kelas dasar karakter
class Karakter:
    def __init__(self, nama, hp, atk):
        self.nama = nama
        self.hp = hp
        self.atk = atk

    def serang(self, target):
        damage = self.atk
        target.hp -= damage
        print(f"{self.nama} menyerang {target.nama} sebesar {damage} damage!")

    def status(self):
        print(f"{self.nama} | HP: {self.hp} | ATK: {self.atk}")


# Kelas pemain (turunan dari Karakter)
class Pemain(Karakter):
    def __init__(self, nama):
        super().__init__(nama, hp=100, atk=15)
        self.exp = 0
        self.level = 1

    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            self.hp += 20
            self.atk += 5
            print(f"Naik Level! Sekarang kamu level {self.level}!")
    
    def status(self):
        print(f"{self.nama} | Level: {self.level} | HP: {self.hp} | ATK: {self.atk} | EXP: {self.exp}")


# Kelas monster
class Monster(Karakter):
    def __init__(self, nama, hp, atk, exp_drop):
        super().__init__(nama, hp, atk)
        self.exp_drop = exp_drop


# Fungsi menjalankan game
def mulai_game():
    nama_pemain = input("Masukkan nama hero kamu: ")
    pemain = Pemain(nama_pemain)

    daftar_monster = [
        Monster("Goblin", 40, 10, 30),
        Monster("Slime", 30, 5, 20),
        Monster("Orc", 60, 15, 50),
    ]

    while True:
        print("\n== STATUS PEMAIN ==")
        pemain.status()
        monster = random.choice(daftar_monster)
        print(f"\nMonster muncul! {monster.nama} | HP: {monster.hp} | ATK: {monster.atk}")

        # Battle
        while monster.hp > 0 and pemain.hp > 0:
            print("\nAksi:")
            print("1. Serang")
            print("2. Keluar")
            aksi = input("Pilih aksi: ")

            if aksi == "1":
                pemain.serang(monster)
                if monster.hp > 0:
                    monster.serang(pemain)
                    print(f"{pemain.nama} sisa HP: {pemain.hp}")
                else:
                    print(f"{monster.nama} dikalahkan!")
                    pemain.exp += monster.exp_drop
                    print(f"Dapat EXP: {monster.exp_drop}")
                    pemain.level_up()
            elif aksi == "2":
                print("Keluar dari game...")
                return
            else:
                print("Pilihan tidak valid!")

        if pemain.hp <= 0:
            print("\nKamu kalah... Game Over.")
            break

# Jalankan game
mulai_game()
