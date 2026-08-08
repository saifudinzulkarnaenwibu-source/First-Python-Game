import time
import random
from senjata import *
from armor import *
from player import *
p_armor = []
p_senjata = []
armor = [
kulit,
besi,
baja,
dwarf,
golem,
dragon,
kratos,
]
senjata = [
karat,
gold,
meteor,
knight,
titan,
cerberus,
freya,
]
armor_g = [
kulit,
besi,
baja,
dwarf,
golem,
dragon,
kratos,
Dev
]
senjata_g = [
karat,
gold,
meteor,
knight,
titan,
cerberus,
freya,
king
]
def toko_armor():
    while True:
        print(f"{'='*49}\n{'TOKO ARMOR':^30} Rp: {player.rp}")
        print(f"{'='*49}\n{'No'}    {'Nama':<9}{'Rarity':<9}{'Healt':<8}{'Deff':<7}{"Harga":<8}\n{'='*49}")
        for no, item in enumerate(armor,1):
            print(f"{no}.    {item.nama:<9}{item.rarity:<9}+{item.hp:<7}+{item.deff}{'%':<5}{item.harga:>4} Rp")
        print(f"{'='*49}")
        pilih = (input(f'[ ENTER ] UNTUK KELUAR\nPILIH >> '))
        if pilih == "":
            print("KAMU KELUAR\n")
            break
        try:
            pilih = int(pilih)
            if 1 <= pilih <= len(armor):
                pilihan = armor[pilih - 1]
            else:
                print(f"\n{'='*49}\n{'Plihan tidak valid':^49}\n{'='*49}\n")
                continue
        except ValueError:
            print(f"\n{'='*49}\n{'Plihan tidak valid':^49}\n{'='*49}\n")
            continue
        if pilihan in player.inventory['armor']:
            print(f"\n{'='*49}\n{f'Kamu sudah punya pedang {pilihan.nama}':^49}\n{'='*49}\n")
        else:
            if player.rp >= pilihan.harga:
                player.rp -= pilihan.harga
                print(f"\n{'='*49}\n{f'Kamu berhasil membeli pedang {pilihan.nama}':^49}\n{'='*49}\n") 
                player.inventory['armor'].append(pilihan)
                continue
            else:
                print(f"\n{'='*49}\n{'Uang mu kurang':^49}\n{'='*49}\n")
                continue
def toko_senjata():
    while True:
        print(f"{'='*49}\n{'TOKO SENJATA':^30} Rp: {player.rp}")
        print(f"{'='*49}\n{'No'}    {'Nama':<9}{'Rarity':<9}{'Atk':<8}{'Pent':<9}{"Harga":<8}\n{'='*49}")
        for no, item in enumerate(senjata,1):
            print(f"{no}.    {item.nama:<9}{item.rarity:<9}+{item.atk:<7}+{item.pent}{'%':<5}{item.harga:>5} Rp")
        print(f"{'='*49}")
        pilih = (input(f'[ ENTER ] UNTUK KELUAR\nPILIH >> '))
        if pilih == "":
            print("KAMU KELUAR\n")
            break
        try:
            pilih = int(pilih)
            if 1 <= pilih <= len(senjata):
                pilihan = senjata[pilih - 1]
            else:
                print(f"\n{'='*49}\n{'Plihan tidak valid':^49}\n{'='*49}\n")
                continue
        except ValueError:
            print(f"\n{'='*49}\n{'Plihan tidak valid':^49}\n{'='*49}\n")
            continue
        if pilihan in player.inventory['senjata']:
            print(f"\n{'='*49}\n{f'Kamu sudah punya pedang {pilihan.nama}':^49}\n{'='*49}\n")
        else:
            if player.rp >= pilihan.harga:
                player.rp -= pilihan.harga
                print(f"\n{'='*49}\n{f'Kamu berhasil membeli pedang {pilihan.nama}':^49}\n{'='*49}\n") 
                player.inventory['senjata'].append(pilihan)
                continue
            else:
                print(f"\n{'='*49}\n{'Uang mu kurang':^49}\n{'='*49}\n")
                continue
def gacha():
    while True:
        print(f"""{f'{'='*10} GACHA {'='*10}':^27}
{f'Rp: {player.rp}':<27}

1. Gacha senjata ( 10.000 )
   Percobaan: {len(p_senjata)}
2. Gacha armor ( 10.000 )
   Percobaan: {len(p_armor)}

3. Riwayat Gacha
4. Info Gacha item

5. Kembali
{'='*27}""")
        pilih = input(f"Pilih: ")
        if pilih == "1":
            if player.rp >= 10000:
                player.rp -= 10000
                item = random.choices(senjata_g,weights=[i.rate for i in senjata_g],k=1)[0]
                p_senjata.append(item)
                if item in player.inventory['senjata']:
                    hasil = "Sudah punya"
                else:
                    player.inventory['senjata'].append(item)
                    hasil = "masuk inventory"
                if item.rarity == 'common':
                    print(f"\n{'='*27}\n{'KAMU DAPAT....':^27}\n{'='*27}\n")
                    time.sleep(0)
                    print(f"""\n{'='*27}
Kamu dapat: 
                          
{item.nama:^27}

Rarity: {item.rarity}
Percobaan: {len(p_senjata)}

Effeck Atk: +{item.atk}
       Pent: +{item.pent}%

{hasil}
{'='*27}
""")
                    continue
                elif item.rarity == 'rare':
                    print(f"\n{'='*27}\n{'KAMU DAPAT....':^27}\n{'='*27}\n")
                    time.sleep(1)
                    print(f"""\n{'='*27}
Selamat Kamu dapat: 
                          
{item.nama:^27}

Rarity: {item.rarity}
Percobaan: {len(p_senjata)}

Effeck Atk: +{item.atk}
       Pent: +{item.pent}%

{hasil}
{'='*27}
""")
                    continue
                elif item.rarity == 'legend':
                    print(f"\n{'='*27}\n{'DAPAT....':^27}\n{'='*27}\n")
                    time.sleep(4)
                    print(f"""\n{'='*27}
Kamu beruntung ⭐
Kamu dapat: 
                          
{item.nama:^27}

Rarity: {item.rarity}
Percobaan: {len(p_senjata)}

Effeck Atk: +{item.atk}
       Pent: +{item.pent}%

{hasil}
{'='*27}
""")
                    continue
                elif item.rarity == 'God':
                    print(f"\n{'='*27}\n{'!@#?$!%#@#%^....':^27}\n{'='*27}\n")
                    time.sleep(6)
                    print(f"""\n{'='*27}
#@%&*?#$%#?
YOU OBTAINED: 
                          
{item.nama:^27}

RARITY: {item.rarity}
ATTEMPTS: {len(p_senjata)}

EFFECK ATK: +{item.atk}
       PENT: +{item.pent}%

{hasil}
{'='*27}
""")
                    continue
            else:
                print(f"\n{'='*27}\n{'Uang mu kurang':^27}\n{'='*27}\n")
        elif pilih == "2":
            if player.rp >= 10000:
                player.rp -= 10000
                item = random.choices(armor_g,weights=[i.rate for i in armor_g],k=1)[0]
                p_armor.append(item)
                if item in player.inventory['armor']:
                    hasil = "Sudah punya"
                else:
                    player.inventory['armor'].append(item)
                    hasil = "masuk inventory"
                if item.rarity == 'common':
                    print(f"\n{'='*27}\n{'KAMU DAPAT....':^27}\n{'='*27}\n")
                    time.sleep(0)
                    print(f"""\n{'='*27}
Kamu dapat: 
                          
{item.nama:^27}

Rarity: {item.rarity}
Percobaan: {len(p_armor)}

Effeck Hp: +{item.hp}
       Def: +{item.deff}%

{hasil}
{'='*27}
""")
                    continue
                elif item.rarity == 'rare':
                    print(f"\n{'='*27}\n{'KAMU DAPAT....':^27}\n{'='*27}\n")
                    time.sleep(1)
                    print(f"""\n{'='*27}
Selamat Kamu dapat: 
                          
{item.nama:^27}

Rarity: {item.rarity}
Percobaan: {len(p_armor)}

Effeck Hp: +{item.hp}
       Def: +{item.deff}%

{hasil}
{'='*27}
""")
                    continue
                elif item.rarity == 'legend':
                    print(f"\n{'='*27}\n{'DAPAT....':^27}\n{'='*27}\n")
                    time.sleep(3)
                    print(f"""\n{'='*27}
Kamu beruntung ⭐
Kamu dapat: 
                          
{item.nama:^27}

Rarity: {item.rarity}
Percobaan: {len(p_armor)}

Effeck Hp: +{item.hp}
       Def: +{item.deff}%

{hasil}
{'='*27}
""")
                    continue
                elif item.rarity == 'God':
                    print(f"\n{'='*27}\n{'!@#?$!%#@#%^....':^27}\n{'='*27}\n")
                    time.sleep(6)
                    print(f"""\n{'='*27}
#@%&*?#$%#?
YOU OBTAINED: 
                          
{item.nama:^27}

RARITY: {item.rarity}
ATTEMPTS: {len(p_armor)}

EFFECK HP: +{item.hp}
       DEFF: +{item.deff}%

{hasil}
{'='*27}
""")
                    continue
            else:
                print(f"\n{'='*27}\n{'Uang mu kurang':^27}\n{'='*27}\n")
                continue
        elif pilih == "5":
            print(f"\n{'='*27}\n{'Kamu Keluar':^27}\n{'='*27}\n")
            break
        elif pilih == "3":
            print(f"\n__riwayat_senjata___")
            if (len(p_senjata)) > 0:
                for no, pa in enumerate(p_senjata,1):
                    print(f"{no}. {pa.nama}")
            else:
                print(f"\n{'Kosong':^19}")
            print(f"\n__riwayat_armor___")
            if (len(p_armor)) > 0:
                for no, paa in enumerate(p_armor,1):
                    print(f"{no}. {paa.nama}")
            else:
                print(f"\n{'Kosong':^17}")
        elif pilih == "4":
            print("\n\n| INFO ITEM SENJATA |")
            for no, ab in enumerate(senjata_g,1):
                print(f"""
{no}. Pedang {ab.nama}
Drop rate: {ab.rate}%
Rarity: {ab.rarity}
Harga: {ab.harga}
Atk: +{ab.atk}
Pent: +{ab.pent}%""")
            print("\n| INFO ITEM ARMOR |")
            for no, ac in enumerate(armor_g,1):
                print(f"""
{no}. Armor {ac.nama}
Drop rate: {ac.rate}%
Rarity: {ac.rarity}
Harga: {ac.harga}
Hp: +{ac.hp}
Def: +{ac.deff}%
""")
        else:
            print(f"\n{'='*27}\n{'Pilihan tidak ada':^27}\n{'='*27}\n")
            continue
                