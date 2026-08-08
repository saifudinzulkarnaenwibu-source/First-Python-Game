from player import player
from musuh import *
lawan = babi
class skill_item():
    def __init__(self, nama, mana, dmg, heal, pent):
        self.nama = nama
        self.mana = mana
        self.dmg = dmg
        self.heal = heal
        self.pent = pent
    def hitung(self):
        dmgg = player.atk * self.dmg
        heall = player.hpa * self.heal
        return dmgg,heall

smash = skill_item("SMASH",         0, 1, 0, 0)
heal = skill_item("HEAL",           40, 0, 0.4, 0)
shot = skill_item("SHOT",           80, 2, 0.3, 0)
fatal = skill_item("FATAL",         80, 2, 0, 100)

player_skill = []
def skill_sistem():
    while True:
        print(f"{'='*30}\n{'PILIH SKILL':^30}\n{'='*30}")
        if len(player.skill_dipakai) < 1:
            player.skill_dipakai.append(smash)
        for no, key in enumerate(player.skill_dipakai,1):
            dmg, heal = key.hitung()
            if heal > 0 and dmg > 0 and key.pent > 0:
                print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Dmg: {int(dmg)}\n   Heal: {int(heal)}\n   Pent: {int(key.pent)}\n")
            elif heal <= 0 and dmg > 0 and key.pent > 0:
                print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Dmg: {int(dmg)}\n   Pent: {int(key.pent)}\n")
            elif heal <= 0 and dmg > 0:
                print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Dmg: {int(dmg)}\n")
            else:
                print(f"{no}. Skill {key.nama}:\n   Mana: {key.mana}\n   Heal: {int(heal)}\n")
        print(f"{'='*30}")
        try:
            pilih = int(input(f'PILIH >> '))
        except ValueError:
            print("PILIHAN TIDAK ADA\n\n\n")
            continue
        if pilih < 1:
            print("PILIHAN TIDAK ADA\n\n\n")
            continue
        try:
            pilihan = player.skill_dipakai[pilih - 1]
        except IndexError:
            print("PILIHAN TIDAK ADA\n\n\n")
            continue
        if pilihan.mana <= player.mana:
            print(f"BERHASIL MEMILIH [ {pilihan.nama} ]")
        else:
            print(f"[ MANA MU KURANG ]\n\n\n")
            continue
        return pilihan