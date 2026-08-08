class senjata_item():
    def __init__(self, pent, atk, harga, rarity, nama, rate):
        self.pent = pent
        self.atk = atk
        self.harga = harga
        self.rarity = rarity
        self.nama = nama
        self.rate = rate
karat = senjata_item(0, 100, 500, "common", "karat", 35)
gold = senjata_item(20, 200, 2000, "common", "gold", 25)
meteor = senjata_item(30, 300, 5000, "common", "meteor", 15)

knight = senjata_item(40, 400, 10000, "rare", "knight", 10)
titan = senjata_item(50, 500, 15000, "rare", "titan", 8)
cerberus = senjata_item(60, 700, 20000, "rare", "cerberus", 5)

freya =  senjata_item(70, 1000, 60000, "legend", "freya", 1.8)

king = senjata_item(100, 1500, float('inf'), "God", "DEV", 0.2)