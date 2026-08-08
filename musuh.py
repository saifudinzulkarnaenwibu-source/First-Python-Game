from player import player
class musuh():
    def __init__(self, hpa, atk, deff, pent, nama, rp, exp):
        self.hpa = hpa
        self.hp = self.hpa
        self.atk = atk
        self.deff = deff
        self.deffa = deff
        self.pent = pent
        self.nama = nama
        self.rp = rp
        self.exp = exp

#NORMAL
babi = musuh(               400,    100,    0,  0,  "Babi hutan",       300,    40)
singa = musuh(              800,    400,    0,  20, "Singa",            600,    70)
badak = musuh(              1000,   300,    20, 0,  "Badak",            700,    80)
beruang = musuh(            1200,   500,    10, 10,  "Beruang",         1000,   100)

Kalajengking = musuh(       200,    100,    10, 30, "Kalajengking",     200,    15)#(9x lawan)
golem = musuh(              4000,   400,    60, 10, "Golem Goa",        1500,   150)
cacing = musuh(             1000,   300,    0,  40, "Cacing",           500,    50)#(4x lawan)
cacing_besar = musuh(       4000,   700,    30,  70, "cacing besar",    2000,   200)
bandit_gurun = musuh(       2500,   500,    20, 50, "Bandit gurun",     1250,   125)#(2x lawan)

guardian = musuh(           3000,   500,    50, 20, "Guardian",         1700,   200)#(2x lawan)
snake_god = musuh(          9000,   1200,   50, 70,  "Snake God",       4000,   500)

#BOSS
kucing = musuh(             3000,   700,    20, 30, "Kucing",           2000,   150)#(Map hutan)
bandit_boss = musuh(        6000,   1200,   20, 60, "Boss Bandit",      3000,   450)#(Map Gurun)
jack = musuh(               9000,   2000,   60, 90, "jack",             10000,  600)#(Spesial boss)

#LAST BOSS
vase_1 = musuh(20000, 2000, 70, 10, "???", 0, 0)
vase_2 = musuh(10000, 4000, 0, 60, "DAN", 0, 0)
vase_3 = musuh(200, 1000, 0, 0, "DAN", 0, 0)

