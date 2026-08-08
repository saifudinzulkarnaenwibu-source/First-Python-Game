class player_power:
    def __init__(self):
        self.hp = 1000
        self.hpa = 1000

        self.atk = 400

        self.mana = 100
        self.manaa = 100

        self.deff = 0
        self.deffa = 0

        self.pent = 0

        self.rp = 100

        self.player_armor = None
        self.player_senjata = None
        self.inventory = {'armor':[],'senjata':[]}

        self.skill_dipakai = []

        self.lv = 1
        self.lv_lama = 1

        self.exp = 0
        self.exp_butuh = 100 

        self.b = None
        self.l = None
        self.k = None

        self.ja = 0
player = player_power()
def status_player():
    print(f'''{'='*23}
{'< Status >':^23}

Lv: {player.lv}
Exp: {player.exp}/{player.exp_butuh}

Hp: {player.hp}/{player.hpa}
Atk: {player.atk}
Mana: {player.mana}/{player.manaa}

RP: {player.rp}
Defence: {player.deff}
Penettasi: {player.pent}

Armor: {"Tidak ada" if player.player_armor is None else player.player_armor.nama}
Senjata: {"Tidak ada" if player.player_senjata is None else player.player_senjata.nama}

{'='*23}
''')
    if len(player.skill_dipakai) > 0:
        print(f'{'='*23}\n{'< Skill dipakai >':^23}')
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
        print(f"{'='*23}")
def exp():
    while player.exp >= player.exp_butuh:
        player.exp -= player.exp_butuh
        player.lv += 1
        player.exp_butuh = int(100 * ( 1.2 ** player.lv))
        if player.lv > player.lv_lama:
            print(f"""
=====( LV UP )=====
LV: {player.lv_lama} > {player.lv}          
MAX HP: +500       
ATK: +200          
MAX MANA: +20     
-------------------
MEMULIHKKAN HP
MEMULIHKAN MANA 
=================== """)
            player.lv_lama += 1
            player.hpa += 500
            player.atk += 200
            player.manaa += 20
            player.mana = player.manaa
            player.hp = player.hpa


