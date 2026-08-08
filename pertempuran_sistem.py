from skill import *
from player import *
from musuh import *
from player import *
from menu import *
player.l = beruang
player.b = "Rei"
player.k = "Kai"
def cek():
    player.l.hp = player.l.hpa
    player.l.deff = player.l.deffa
    player.deff = player.deffa
    player.mana = player.manaa
def sistem_tempur_new():
        while player.hp > 0 and player.l.hp > 0:
            print(f"""
[ PLAYER ]
HP: {player.hp}/{player.hpa}
ATK: {player.atk}
MANA: {player.mana}/{player.manaa}
PENT: {player.pent}%
DEF: {player.deff}%""")
            if player.b is not None:
                print(f"""
[ {player.b} ]
ATK: {player.atk * 30 // 100}
PENT: 50%""")
            if player.k is not None:
                print(f"""
[ {player.k} ]
Heal: {player.hpa * 10 // 100 }
Coin: +30%""")
            print(f"""
[ Musuh | {player.l.nama} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk}
PENT:{player.l.pent}%
DEF:{player.l.deff}%
""")
            print(f"{'-'*30}\nMusuh melihat keberadaan mu\nkalahkan dia!\n{'-'*30}\n")
            while player.hp > 0 and player.l.hp > 0:
                hasil = skill_sistem()
                dmg, heal = hasil.hitung()
                player.mana -= hasil.mana
                defen = max(0, player.l.deff - (hasil.pent + player.pent))
                player.hp += heal
                if player.hp > player.hpa:
                    player.hp = player.hpa
                player.l.hp -= dmg - ( dmg * defen // 100)
                if heal > 0:
                    print(F"\nPlayer berhasil memulihkan {heal} hp")
                if dmg > 0:
                    print(F"\nPlayer berhasil memberi {dmg - (dmg * defen // 100)} dmg")
                if player.b is not None:
                    defenb = max(0, player.l.deff - 50)
                    player.l.hp -= (player.atk * 30 // 100) - ((player.atk * 30 // 100) * defenb // 100)
                    print(f"{player.b} berhasil memberi {(player.atk * 30 // 100) - ((player.atk * 30 // 100) * defenb // 100) } dmg")
                if player.k is not None:
                    player.hp = min(player.hp + player.hpa * 10 // 100, player.hpa)
                    print(f"{player.k} berhasil memulihkan {player.hpa * 10 // 100} hp")
                if player.l.hp > 0:
                    print(f"""
[ Musuh | {player.l.nama} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk}
""")
                    time.sleep(3)
                else:
                    player.l.hp = 0
                    time.sleep(2)
                    print(f"""
[ Musuh | {player.l.nama} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk} 
""")
                    print(F"{player.l.nama} berhasil dikalahkan\n")
                    if player.k is not None:
                        print(f"{player.k} memberi {player.l.rp * 30 // 100} Rp ")
                        player.rp += (player.l.rp * 30 // 100)
                    print(F"Kamu memdapatkan {player.l.rp} Rp")
                    print(f"Kamu mendapatkan {player.l.exp} Exp")
                    player.rp += player.l.rp
                    player.exp += player.l.exp
                    break
                ddof = max(0, player.deff - player.l.pent)
                print(f"{player.l.nama} menyerang mu \n{player.l.atk - (player.l.atk * ddof // 100)} dmg diterima")
                player.hp -= player.l.atk - (player.l.atk * ddof // 100)
                print(f"""
[ PLAYER ]
HP:{player.hp}/{player.hpa}
ATK:{player.atk}
MANA:{player.mana}/{player.manaa}
""")
                if player.hp <= 0:
                    print("Kamu kalah")
                    break
                exp()
def sistem_tempur_new_pro_max():
        jumlah_lawan = player.ja
        while player.hp > 0 and jumlah_lawan > 0:
            print(f"""
[ PLAYER ]
HP: {player.hp}/{player.hpa}
ATK: {player.atk}
MANA: {player.mana}/{player.manaa}
PENT: {player.pent}%
DEF: {player.deff}%""")
            if player.b is not None:
                print(f"""
[ {player.b} ]
ATK: {player.atk * 30 // 100}
PENT: 50%""")
            if player.k is not None:
                print(f"""
[ {player.k} ]
Heal: {player.hpa * 10 // 100 }
Coin: +30%""")
            print(f"""
[ Musuh | {player.l.nama} | x{jumlah_lawan} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk * jumlah_lawan}
PENT:{player.l.pent}%
DEF:{player.l.deff}%
""")
            print(f"{'-'*30}\nMusuh melihat keberadaan mu\nkalahkan dia!\n{'-'*30}\n")
            while player.hp > 0 and player.l.hp > 0:
                hasil = skill_sistem()
                dmg, heal = hasil.hitung()
                player.mana -= hasil.mana
                defen = max(0, player.l.deff - (hasil.pent + player.pent))
                player.hp += heal
                if player.hp > player.hpa:
                    player.hp = player.hpa
                player.l.hp -= dmg - ( dmg * defen // 100)
                if heal > 0:
                    print(F"\nPlayer berhasil memulihkan {heal} hp")
                if dmg > 0:
                    print(F"\nPlayer berhasil memberi {dmg - (dmg * defen // 100)} dmg")
                if player.b is not None:
                    defenb = max(0, player.l.deff - 50)
                    player.l.hp -= (player.atk * 30 // 100) - ((player.atk * 30 // 100) * defenb // 100)
                    print(f"{player.b} berhasil memberi {(player.atk * 30 // 100) - ((player.atk * 30 // 100) * defenb // 100) } dmg")
                if player.k is not None:
                    player.hp = min(player.hp + player.hpa * 10 // 100, player.hpa)
                    print(f"{player.k} berhasil memulihkan {player.hpa * 10 // 100} hp")
                time.sleep(2)
                if player.l.hp > 0:
                    print(f"""
[ Musuh | {player.l.nama} | x{jumlah_lawan} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk * jumlah_lawan}
""")
                    time.sleep(3)
                else:
                    jumlah_lawan -= 1
                    if jumlah_lawan <= 0:
                        time.sleep(2)
                        player.l.hp = 0
                        print(f"""
[ Musuh | {player.l.nama} | x{jumlah_lawan} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk} 
""")
                        print(F"Semua {player.l.nama} berhasil dikalahkan\n")
                        if player.k is not None:
                            print(f"{player.k} memberi {(player.l.rp * player.ja)* 30 // 100} Rp ")
                            player.rp += ((player.l.rp*player.ja) * 30 // 100)
                        print(F"Kamu memdapatkan {player.l.rp*player.ja} Rp")
                        print(f"Kamu mendapatkan {player.l.exp*player.ja} Exp")
                        player.rp += player.l.rp*player.ja
                        player.exp += player.l.exp*player.ja
                        break
                    print(f"\nSatu {player.l.nama} berhasil dikalahkan")
                    player.l.hp = player.l.hpa
                    print(f"""
[ Musuh | {player.l.nama} | x{jumlah_lawan} ]
HP:{player.l.hp}/{player.l.hpa}
ATK:{player.l.atk * jumlah_lawan}
""")
                ddof = max(0, player.deff - player.l.pent)
                print(f"{player.l.nama} menyerang mu \n{(player.l.atk * jumlah_lawan) - ((player.l.atk*jumlah_lawan) * ddof // 100)} dmg diterima")
                player.hp -= (player.l.atk*jumlah_lawan) - ((player.l.atk*jumlah_lawan) * ddof// 100)
                print(f"""
[ PLAYER ]
HP:{player.hp}/{player.hpa}
ATK:{player.atk}
MANA:{player.mana}/{player.manaa}
""")
                if player.hp <= 0:
                    print("Kamu kalah")
                    break
                exp()