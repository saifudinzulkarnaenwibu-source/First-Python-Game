class armor_item():
    def __init__(self, deff, hp, harga, rarity, nama, rate):
        self.deff = deff
        self.hp = hp
        self.harga = harga
        self.rarity = rarity
        self.nama = nama
        self.rate = rate
kulit = armor_item(0, 500, 600, "common", "kulit", 35)
besi = armor_item(10, 600, 2000, "common", "besi", 25)
baja = armor_item(20, 1300, 4000, "common", "baja", 15)

dwarf = armor_item(30, 2500, 8000, "rare", "dwarf", 10)
golem = armor_item(35, 4000, 12000, "rare", "golem", 8)
dragon = armor_item(40, 6000, 18000, "rare", "dragon", 5)

kratos =  armor_item(50, 9000, 40000, "legend", "kratos", 1.8)

Dev = armor_item(70, 200000, float('inf'), "God", "Dev", 0.2)

