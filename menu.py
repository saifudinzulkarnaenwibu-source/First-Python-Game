from toko_sistem import *
from player import *
from inventory import *
from skill import *
def menu():
    while True:
        pilih = input(f'''{'='*27}
{'[ MAIN MENU ]':^23}

1. Toko senjata
2. Toko armor
3. Gacha

4. Status player
5. Inventory

6. Kembali
{'='*27}
Pilih >> ''')
        print("")
        if pilih == "1":
            toko_senjata()
        elif pilih == "2":
            toko_armor()
        elif pilih == "3":
            gacha()
        elif pilih == "4":
            while True:
                status_player()
                pilih = input("ENTER >> ")
                print("")
                break
        elif pilih == "5":
            inventory()
        elif pilih == "6":
            print("[ Kembali kecerita... ]")
            break
        elif pilih == "q":
            player.rp = float("inf")
        else:
            print(f"{'='*27}\n{'Pilihan gagal':^27}\n{'='*27}\n")
            continue