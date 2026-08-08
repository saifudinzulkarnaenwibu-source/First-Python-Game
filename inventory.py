from player import *
from skill import *
def inventory():
    while True:
        masuk = input(f'''{'='*27}
{'( INVENTORY )':^23}

1. Inventory senjata
2. Inventory armor
3. Iventory skill

4. Kembali
{'='*27}
Pilih >> ''')
        print("\n\n")
        if masuk == "1":
            while True:
                print(f"{'='*40}\n{'INVENTORY SENJATA':^40}\n{'='*40}")
                if len(player.inventory['senjata']) > 0:
                    for no, item in enumerate(player.inventory['senjata'],1):
                        print(f"{no}. Senjata {item.nama}\nRarity: {item.rarity}\nAtk: +{item.atk}\nPent: +{item.pent}%\n")
                else:
                    print(F"\n\n{'INVENTORY KOSONG':^40}\n\n")
                pilih = (input(f'{'='*40}\n[ ENTER ] UNTUK KELUAR\n[ L ] Untuk melepas senjata\nPILIH >> '))
                if pilih == "L":
                    if player.player_senjata is not None:
                        obj = player.player_senjata
                        player.atk -= obj.atk
                        player.pent -= obj.pent
                        player.player_senjata = None
                        print(f"\n\n{'='*40}\n{f'Kamu melepas senjata':^40}\n{'='*40}\n\n")
                        continue
                    else:
                        print(f"\n\n{'='*40}\n{f'Kamu tidak memakai senjata':^40}\n{'='*40}\n\n")
                        continue
                if pilih == "":
                    print("KAMU KELUAR\n\n\n")
                    break
                try:
                    pilih = int(pilih)
                    if 1 <= pilih <= len(player.inventory['senjata']):
                        pilihan = player.inventory['senjata'][pilih - 1]
                    else:
                        print(f"\n\n{'='*40}\n{'Pihan tidak valid':^40}\n{'='*40}\n\n")
                        continue
                except ValueError:
                    print(f"\n\n{'='*40}\n{'Pihan tidak valid':^40}\n{'='*40}\n\n")
                    continue
                if player.player_senjata is None:
                    player.player_senjata = pilihan
                    obj = player.player_senjata
                    player.atk += obj.atk
                    player.pent += obj.pent
                    print(f"\n\n{'='*40}\n{f'Kamu memakai senjata {obj.nama}':^40}\n{'='*40}\n\n")
                    continue

                else:
                    print(f"\n\n{'='*40}\n{f'Kamu sudah memakai senjata':^40}\n{'='*40}\n\n")
                    continue
        elif masuk == "2":
            while True:
                print(f"{'='*40}\n{'INVENTORY ARMOR':^40}\n{'='*40}")
                if len(player.inventory['armor']) > 0:
                    for no, item in enumerate(player.inventory['armor'],1):
                        print(f"{no}. Armor {item.nama}\n   Rarity: {item.rarity}\n   Hp: +{item.hp}\n   Def: +{item.deff}%\n")
                else:
                    print(F"\n\n{'INVENTORY KOSONG':^40}\n\n")
                pilih = (input(f'{'='*40}\n[ ENTER ] UNTUK KELUAR\n[ L ] UNTUK MELEPAS ARMOR\nPILIH >> '))
                if pilih == "L":
                    if player.player_armor is not None:
                        obj = player.player_armor
                        player.hpa -= obj.hp
                        player.deff -= obj.deff
                        player.deffa -= obj.deff
                        player.player_armor = None
                        print(f"\n\n{'='*27}\n{f'Kamu melepas armor':^40}\n{'='*40}\n\n")
                        continue
                    else:
                        print(f"\n\n{'='*27}\n{f'Kamu tidak memakai armor':^40}\n{'='*27}\n\n")
                        continue
                if pilih == "":
                    print("KAMU KELUAR\n\n\n")
                    break
                try:
                    pilih = int(pilih)
                    if 1 <= pilih <= len(player.inventory['armor']):
                        pilihan = player.inventory['armor'][pilih - 1]
                    else:
                        print(f"\n\n{'='*40}\n{'Pihan tidak valid':^40}\n{'='*40}\n\n")
                        continue
                except ValueError:
                    print(f"\n\n{'='*40}\n{'Pihan tidak valid':^40}\n{'='*40}\n\n")
                    continue
                if player.player_armor is None:
                    player.player_armor = pilihan
                    obj = player.player_armor
                    player.hpa+= obj.hp
                    player.deff += obj.deff
                    player.deffa += obj.deff
                    print(f"\n\n{'='*40}\n{f'Kamu memakai armor {obj.nama}':^40}\n{'='*40}\n\n")
                    continue

                else:
                    print(f"\n\n{'='*40}\n{f'Kamu sudah memakai armor':^40}\n{'='*40}\n\n")
                    continue
        elif masuk == "3":
            while True:
                print(f"{'='*30}\n{'INVENTORY SKILL':^30}\n{'='*30}")
                for no, key in enumerate(player_skill,1):
                    dmg, heal = key.hitung()
                    if key.heal > 0 and dmg > 0 and key.pent > 0:
                        print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Dmg: {int(dmg)}\n   Heal: {int(heal)}\n   Pent: {int(key.pent)}\n")
                    elif key.heal <= 0 and dmg > 0 and key.pent > 0:
                        print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Dmg: {int(dmg)}\n   Pent: {int(key.pent)}\n")
                    elif key.heal <= 0 and dmg > 0:
                        print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Dmg: {int(dmg)}\n")
                    else:
                        print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Heal: {int(key.heal)}\n")
                print(f"{'='*30}")
                pilih = (input(f'[ ENTER ] UNTUK KELUAR\nPILIH SKILL UNTUK DIPAKAI\nPILIH >> '))
                if pilih == "":
                    print("KAMU KELUAR\n\n\n")
                    break
                try:
                    pilih = int(pilih)
                except ValueError:
                    print("PILIHAN TIDAK ADA\n\n\n")
                    continue
                if pilih < 1:
                    print("PILIHAN TIDAK ADA\n\n\n")
                    continue
                try:
                    pilihan = player_skill[pilih - 1]
                except IndexError:
                    print("PILIHAN TIDAK ADA\n\n\n")
                    continue
                if (len(player.skill_dipakai) + 1) > 3:
                    print(f"SKILL SUDAH PENUH\n\n\n")
                else:
                    if pilihan not in player.skill_dipakai:
                        player.skill_dipakai.append(pilihan)
                        print(f"BERHASIL MEMILIH [ {pilihan.nama} ]\n\n\n")
                    else:
                        print(f"KAMU SUDAH MEMAKAI [ {pilihan.nama} ]\n\n\n")

                

        elif masuk == "4":
            break
        