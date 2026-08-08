from player import *
from menu import *
from pertempuran_sistem import sistem_tempur_new, sistem_tempur_new_pro_max, cek
import time
player.b = None
player.k = None
def war():
    sistem_tempur_new()
    cek()
    exp()
    time.sleep(3)
def warp(): 
    sistem_tempur_new_pro_max()
    cek()
    exp()
    time.sleep(3)
while player.hp > 0:
    if player.hp <= 0:
        break
    while True:
        print(f"""

    Informasi penting
    1. Tampilan menu tidak dapat dimunculkan oleh player, hanya muncul jika sampai ketitik story tertentu, jadi jangan sia siakan tampilan
    menu yang muncul.

    2. Sistem dalam tampilan menu
    - Toko & Gacha
    disini adalah tempat kamu bisa menggunakan uang mu, untuk mendapatkan armor atau senjata.
    - Status player
    digunakan untuk melihat stat keseluruhan player dan skill yang sedang digunakan untuk pertempuran.
    - Inventory 
    Tempat semua barang dan skill mu berada, masuk kedalam inventory jika ingin memakai armor, senjata, atau skill yang dipunyai.

    3. Game ini bukanlah game yang memiliki banyak tombol, pilihan player memilih hanya ada jika diminta.

    4. Pembuat game adalah saya saat 16 tahun, memulai membuat game ini hanya dengan hp, terimakasih jika anda telah mencoba game 
    saya yang membosankan ini, saya harap bisa membuat game lain yang lebih bagus dan intraktif.
    """)
        ww = input("ENTER >> ")
        break
    while True:
        nama = input("\nmasukan nama anda: ")
        if len(nama) <= 10:
            break
        else:
            print("\nTerlalu panjang\n")
    p = f"{nama:<10}"
    w = f"{'???':<10}"
    a = f"{'Admin':<10}"
    r = f"{'Rei':<10}"
    j = f"{'Jack':<10}"
    time.sleep(3)
    print(f"\n{'[ PROGRAM DIMULAI ]'}")
    time.sleep(3)

    print(f"""
    {p}: Wow aku beneran masuk kedalam game 
    {p}: Ternyata cara yang ada di internet itu real
    {p}: Oke, sekarang aku dimana?..""")
    time.sleep(3)
    print(f"""
    {p}: Halo sir apa kamu tau ini dimana?..
    {w}: Ini adalah kota roma, Apakah kau baru disini?
    {p}: Ya, saya baru disini
    {w}: Ini bukan kota yang indah, pilihan buruk jika kau kesini untuk berlibur
    {p}: Ada apa di kota ini??
    {w}: Pergi lah ke guild jika ingin tau lebih jauh, kebetulan aku ingin pergi ke guild, kau mau ikut?
    {p}: Ya, tentu""")
    time.sleep(3)
    print(f"\n{'[ ROMA ADVENTURE GUILD | Senin ]'}")
    print(f"""
    {w}: Ini guildnya, sekarang aku akan pergi
    {p}: Oke terimakasih sir...
    {w}: Jack
    {p}: Ya good, terimakasih jack.""")
    time.sleep(3)
    print(f"""
    {w}: Hei kamu, kemari
    {p}: Saya?
    {w}: Iyaaa...
    {w}: Kamu kelihatan memiliki banyak pertanyaan, aku akan membantu mu, tentu dangan bayaran..
    {p}: Apakah kamu cenayang?, aku memiliki segudang pertanyaan dibenak ku
    {p}: Bisa kamu beritahu aku tuntang dunia ini?
    {w}: Pertanyaan apa itu?, apa kamu berasal dari desa sangat terpecil, hingga hal seperti itu perlu ditanyakan
    {w}: Tapi baiklah aku akan menjawabnya, bagaimana dengan 20 koin emas? 
    {p}: Aku tidak tau berapa nilai uang itu, tapi aku punya hall yang jauh lebih berharga!..""")
    time.sleep(3)
    print(f"""
    {w}: Wos apa itu?, aku tidak pernah melihat benda itu selama aku hidup
    {p}: Ini adalah phone, barang berteknologi super tinggi dan hanya ada 1 di dunia
    {w}: Aku tau kamu berbohong, tapi barang itu pasti berharga lebih dari 20 koin emas
    {w}: Nama ku Rei, and..
    {p}: Aku {nama}.""")
    time.sleep(3)
    print(f"""
    {r}: Dunia ini sekarang 60% dikuasai oleh Dewm, orang yang mengaku adalah tuhan
    {r}: 40% sisa adalah orang yang tidak percaya oleh dia, kota ini adalah salah satunya
    {r}: Kamu beruntung tidak salah jalan ke tempat kekuasaan dia, dia memajak warganya sangat tinggi
    {r}: Dan katanya dia juga tau segala hal di dunia ini
    {r}: Raja kota ini mulai mengumpulkan orang untuk mengalahkan dia
    {p}: Apa kau tertarik mengalahkan dia?
    {r}: Tidak, aku lebih tertarik dengan pemikirannya
    {p}: Bagus, apa kamu mau berpetualang dengan ku untuk menemui dia?
    {r}: Apa kamu gilaa!?..
    {r}: Untuk sampai sana kita perlu melewati gurun dan tample tempatnya tinggal, petualang Tier S saja tidak berhasil
    {p}: Tidak tahu sampai kita mencoba kan?.. 
    {p}: Lagi pula kita kesana bukan untuk bertarung
    {r}: Dasar aneh, aku akan ikut, aku rasa kamu adalah mesias yang datang dari dunia lain 
    {p}: Hahaha, bukan dong.. [ Buset cenayang nih orang???.. ]""")
    time.sleep(3)
    print(f"""
    {r}: Ambil ini [ Pedang karat diberi ]
    {r}: Agar kau tidak bertarung dengan tangan kosong, lagi pula aku akan ganti dengan yang baru
    {p}: Oke, makasih
    {p}: Kapan kita akan pergi, kau tau arah kesana?
    {r}: Eemm.... yaa ya aku tau, kita akan pergi besok, aku ingin menghabiskan uang ku dulu
    {r}: nanti Kita akan melewati hutan, ayo nanti kita latih kemampuan mu
    {p}: Bagaimana kau tau aku tidak bisa tarung..
    {p}: yaudahlah, sampai ketemu besok""")
    player_skill.append(smash)
    player.inventory["senjata"].append(karat)

    print(f"""
    Informasi bantuan
    1. Kamu tadi mendapatkan senjata, jadi coba pakai senjatamu 
    cara: - masuk ke inventory
        - pilih inventory senjata
        - pilih senjata yang ingin dipakai
    2. Kamu memiliki skill terpendam yang belum dipakai
    cara: - masuk ke inventory
        - piih inventory skill
        - pilih skill yang ingin dipakai
    3. Cek status lengkap mu, kamu dapat melihat senjata dan skill yang kamu pakai
    cara: - masuk ke status player
        - selesai
        """)
    menu()
    time.sleep(3)
    print(f"\n{'[ DIDEPAN ROMA ADVENTURE GUILD | Selassa ]'}")
    print(f"""
    {p}: Sampe juga dia.....
    {p}: Gila bawaan lu banyak amat
    {r}: Ini termasuk normal untuk orang yang ingin melewati benua, tidak seperti orang didepan ku ini
    {p}: Hehe, tenang aku lumayan jago masak, untuk masalah makanan itu aman
    {r}: Ya ya ya, ayo kita pergi""")
    time.sleep(3)
    print(f"\n{'[ Hutan Timur | Kamis ]'}")
    print(f"""
    {r}: Ayo istirahat sebentar, lihat disana ada babi hutan?
    {r}: Tangkap dia, itu akan jadi latihan pertama mu
    {p}: Mudah""")
    time.sleep(3)
    player.l = babi
    war()
    time.sleep(3)
    print(f"""
    {r}: Sepertinya 1 kurang cari yang lain
    {p}: Boleh ku tau fungsi mu apa?
    {r}: Asal kau tau saat kau nangkep tu babi aku udah nangkep 5 kelinci
    {p}: Oke""")
    time.sleep(3)
    player.l = babi
    player.ja = 2
    warp()
    print(f"""
    {p}: Hey lihat, aku bawa 2 babi
    {r}: Bagus, lihat makanannya sudah jadi
    {p}: Ya, terimakasih
    {p}: Hey tadi sepertinya aku naik lv
    {r}: Pppff... 
    {r}: Mana ada kayak gitu, lu kira kita lagi dalam game huh
    {r}: Dari yang kulihat kemampuan mu setara petualang tier C, dan itu tinggi
    {p}: ooh bagus, orang yang tidak pernah bertarung punya tier C, bagaimana dengan mu?
    {r}: Aku tier B, 1 diatas mu
    {r}: Mungkin besok aku sudah tersusul, hahaha...
    {p}: Dari kemampuan mungkin iya, tapi tidak dengan penyalaman 
    {p}: Dan otak mu ada jauh di atas ku
    {r}: Terimakasih, Ayo lanjutkan perjalanan kita""")
    time.sleep(3)
    print(f"\n{'[ Hutan tengah | Senin ]'}")
    print(f"""
    {p}: hey lihat sepertinya ada pesta disana
    {r}: Badan besar, kasar, dan bercula...
    {r}: Ku kira kita menemukan sekumpulan badak liar disini
    {p}: Apakah itu bagus?
    {r}: Iyaa, mereka selalu dicari oleh petualang lain, exp yang didapat darinya besar dan juga kita berkemungkinan dapet armor
    {p}: Apakah mereka kuat?
    {r}: Mereka sangat kuat jika bersama, tapi untung lah mereka tidak sepintar kita manusia
    {r}: Yang kita perlukan hanyalah menarik perhatiannya satu per satu
    {p}: Ayo, sebelum petualang lain melihat""")
    time.sleep(3)
    player.b = "Rei"
    player.l = badak
    war()
    player.inventory["armor"].append(kulit)
    print(f"""
    {r}: Lihat apa yang kudapatkan, armor kulit hanya dalam sekali percobaan?
    {r}: What a lucky, aku tidak akan memakai ini jadi kau saja yang ambil
    {p}: Lalu apa yang kau dapatkan?
    {r}: Aku dapat culanya dan exp
    {p}: Jelas itu lebih sedikit dari yang kudapat
    {r}: Aman aja, orang pro mah gini
    {r}: Kamu pasti terluka tadi coba pake skill heal
    {p}: Gimana caranya?
    {r}: Harusnya sekarang kamu bisa pake sih
    {p}: Nanti ku cek 
    {r}: Ini ada ku kasih duit buat kamu gacha
    {p}: Why?
    {r}: Gatau, pengen aja ngasih, langian aku udah kaya [ +9000 Rp ]
    """)
    player.rp += 10000
    player_skill.append(heal)
    menu()
    time.sleep(3)
    print(f"\n{'[ Hutan tengah | Kamis ]'}")
    print(F"""
    {p}: Apakah perjalanan kita masih lama?
    {r}: Ya, mungkin ada beberapa bulan lagi
    {r}: Tapi kita akan keluar dari hutan ini sebentar lagi
    {p}: Oh oke
    {p}: Rei kamu udah bertualang dari kapan?
    {r}: Sejak umurku masih 13 ayah ku sudah sering ngajak aku berpetualang
    {r}: Tapi itu hanya sebertar, sam...
    {p}: Kita diserang""")
    time.sleep(3)
    player.l = singa
    war()
    print(f"""
    {r}: Pantas saja mereka sangat pintar, mereka punya kapten
    {r}: Apakah kau bisa ngalahin dia?
    {p}: Iya kayaknya
    {r}: Biar aku ngalahin kroconya
    """)
    time.sleep(3)
    player.b = None
    player.l = kucing
    war()
    k = f"{'Kucing':<10}"
    print(f'''
    {p}: Lawan yang sulit, tapi aku berhasil
    {r}: Iya susah, harusnya aku bawa lebih banyak orang
    {p}: Betul juga
    {r}: Aku kemaren ngambil misi, buat ngambil madu legend
    {p}: Susah gak?
    {r}: Lebih gampang dari kucing tadi, kita cuman perlu rebut dari beruang
    {p}: Imbalannya apa emang?
    {r}: Uang 4000 Rp, lumayan lah buat misi
    {p}: Ayo deh
    {p}: .......
    {p}: Reeeii kucingnyaa bangun lagi
    {r}: Tenang biar aku yang urus
    {k}: Iyaa bg ampun
    {r}: Mau gak ikut kita?
    {k}: Gas [ dev males bikin drama ]
    {p}: Oke kita dapet rekan baru?
    {r}: Iya kasih nama apa yah
    ''')
    kk = input("Masukan nama untuk sikucing: ")
    time.sleep(3)
    player.k = kk
    x = f"{f'{kk}':<10}"
    print("")
    print(f"""
    {p}: Kekuatan mu apa {kk}
    {x}: Aku bisa ngeheal selama pertarungan
    {p}: Seberapa besar? 
    {x}: 10% max hp
    {p}: Kecil amat
    {r}: Itu termasuk op loh
    {r}: Jarang ada hewan yg punya skill heal
    {x}: Dia bener, tapi aku kesel
    {x}: Tujuan kalian apa emang?
    {p}: Pengen ke..
    {p}: Kemana dah lupa aku
    {r}: Kelas, kita mau ke tempat dewm
    {x}: Ngapain dah?
    {x}: Dia pemimpin yang baik, bukannya justru rajamu yang harusnya dikalahin
    {p}: Huhh..?
    {r}: ....
    {r}: Jadi kau bilang pemipin mu adalah orang baik yang memajak warganya sangat tinggi?
    {x}: Pajak tinggi bukan berarti buruk
    {x}: Ayo udh lanjut aja [ dev males lanjutin obrolan ]
    {p}: Gass""")
    time.sleep(3)
    print(f"\n{'[ Hutan perbatasan | senin ]'}")
    print(f"""
    {p}: Liat sepertinya itu beruang yang kau bilang kemaren
    {r}: Ayo, sekalian liat kemampuan si {kk}
    {k}: Oke ayo""")
    time.sleep(3)
    player.l = beruang
    player.b = "Rei"
    player.k = kk
    war()
    print(f"\n{'[ Gurun | Rabou ]'}")
    print(f"""
    {p}: Sampe juga gurun, perjalanan disini bakal berapa lama?
    {r}: Sekitar 3 bulan, itu juga kalo hidup
    {p}: Lama yah, nanti minum gimana?
    {r}: Buat itu aman kita bisa minum air dari kaktus atau monster
    {p}: Gaak ada air normal?
    {k}: Air kencicng
    {p}: Itu pilihan terakhir yang paling gak normal
    {r}: ...
    {r}: Nanti ditengah gurun kita bakal nemu desa kok, ada sumur disono, kita bisa istirahat disana
    {r}: Sekalian ngambil hadiah dari misi beruang kemarin
    {p}: Syukurlah, ayo jalan cepet cepet, aku pengen cepet tidur dikasur, dan makan makanan enak""")
    time.sleep(3)
    print(f"\n{'[ Gurun tengah | Sabtu ]'}")
    print(f"""
    {k}: Lihat itu..
    {r}: Gila... itu adalah badai pasir terbesar yang pernah kulihat
    {r}: Kita dalam bahaya, ayo cari tempat berlindung
    {p}: Ada goa kecil disono, ayo pergi
    {r}: Ayo""")
    print(f"\n{'[ Goa | Sabtu ]'}")
    print(f"""
    {r}: Kita bisa istirahat disini
    {p}: Ya semuga tidak ada monster disini
    {k}: Hahaha, lain kali harusnya kau tidak berdoa {nama}
    {k}: Ada puluhan kalajengking disini
    {r}: Lari atau Lawan?
    {p}: Nanya gw?
    {r}: Iya lu paling kuat soalnya
    """)
    pilih = input(f"[ A.Lari kedalam gua ] [ B.Lawan! ]\nPilih >> ")
    if pilih == "A":
        print(f"\n{'[ Goa dalam | Sabtu ]'}")
        print(f"""
    {r}: Sepertinya sudah aman
    {p}: coba nyalain api, gelap banget
    {r}: Oke, aku buat perapian
    {k}: Ahahaahhahaha
    {r}: ......
    {p}: ......
    {k}: Udah kutebak pilihan tu orang emang gak pernah bener """)
        player.l = golem
        player.b = "Rei"
        player.k = kk
        war()
        print(f"""
    {p}: Selesai juga, tebel banget badannya gila
    {r}: Kita perlu senjata lebih bagus 
    {p}: {kk} Kamu mvpnya kali ini
    {r}: Iya dmg kecilnya jadi gak berasa
    {k}: Hehe
    {r}: Hey lihat, apa yang ada di belakang golem tadi
    {p}: ?
    {r}: Book skil legendry
    {p}: Sepertinya pilihan ku kali ini tidak salah huh
    {k}: Tch
    {r}: Ini ambil [ Skil fatal didapat ]
    {p}: Oke
    {k}: Badai sudah berhenti ayo, keluar
    {p}: Tau dari?
    {k}: Baunya
    {r}: Kemana kita nanti?
    {r}: Desa
    {p}: Akhirrnyaa, instirahat..
    {k}: Ayooooo""")
        player_skill.append(fatal)
        apaan = None
        time.sleep(3)
    if pilih == "B": 
        print(f"""
    {r}: Aku akan lawan setengahnya
    {p}: Oke
    {k}: Aku kabur aja ya
    {r}: Ikut aku {kk} """)
        player.l = Kalajengking
        player.b = None
        player.k = None
        player.ja = 9
        warp()
        print(f"""
    {p}: Fuufh selesai juga
    {r}: Iya, sisa 1 lagi dilawan {kk}
    {k}: Bantuin woy!..
    {p}: hey lihat bada udah selesai
    {r}: Kayak ada orang
    {p}: .....
    {p}: Itu Jack
    {r}: Kenalan mu? apa dia udah gila
    {p}: Dia orang yang mempertemukan dia
    {r}: Ayo temui dia
    {p}: Woi jack lu ngapain ditengah badai pasir?
    {j}: Bukan masalah besar, aku cuman kejebak
    {k}: [ Mayat apa itu? ]
    {p}: Lu gpp?
    {j}: Iya, kalian mau kemana
    {r}: Desa rekal, lu kemana
    {j}: Sama
    {p}: Ayo bareng
    {j}: Gak dulu, makasih
    {p}: Oke..
    {k}: Woy bantuin dulu ini...
    {r}: Iyaa iyaa, dah
    {p}: Ayo lanjut""")
        apaan = "ada"
        rr = "Rei"
    time.sleep(3)
    dd = f"{'mskdcs':<10}"
    print(f"\n{'[ Desa tengah gurun | jumat ]'}")
    print(f"""
    {r}: Kita sampai
    {r}: {nama} dan {kk} kalian cari penginapan, aku akan keguild nukerin misi dan nyari misi lain.
    {r}: Kita bertemu lagi disini nanti sore
    {p}: Okee, makasih aku berhutang pada mu
    {k}: Ayo {nama}.....
    {p}: Makan apa ya kita
    {k}: Ayo cari yang paling rame!
    {p}: Gaass..""")
    time.sleep(3)
    print(f"\n{'[ Penginapan Desa | jumat ]'}")
    print(f"""
    {r}: Ini imbalan mu, untuk misi yang ada memburu beruang kemarin [ 2000Rp diberikan ]
    {p}: Oke makasih, lalu apa misi baru yang kamu dapatkan
    {r}: Hampir kebanyakan misi disono adalah misi kroco, kecuali 1, ini adalah misi global yg bisa diambil beberapa orang sekaligus
    {r}: Menangkap pembunuh Desert god, tidak ada petunjuk dari guild.
    {p}: Lalu bagaimana orang akan menangkap dia?
    {r}: Entah kita harus cari tau sendiri.
    {p}: {rr}, ayo kita ke toko peralatan bareng besok
    {r}: Eee, ayo
    {k}: Terus gua? enak amat lu malah berduaan
    {p}: Jagain barang aja ya
    {k}: Aaggh, besoknya gw yang keluar ya
    {p}: Iyaa
    {r}: pff.. hahahaha
    {p}: ... :)""")
    player.rp += 2000
    time.sleep(3)
    menu()
    print(f"\n{'[ penginapan desa | sabtu ]'}")
    print(f"""{k}: Sialan mereka malah pergi berduaan [ dev males bikin cerita romance]""")
    if apaan is not None:
        print(f"""{k}: Kemaren mayat apaan dah? apa ada hubungannya sama misi tadi yang dibilang
    {k}: Perlu gw seledikin ini
    {k}: Wow, sepertinya Gw bener [ dev males misahin tempat ]
    {k}: Ini mayat desert god
    {k}: Gw harus mengingat ini""")
    time.sleep(3)
    print(f"\n{'[ penginapan desa | minggu ]'}")
    print(f"""
    {p}: Kapan kita lanjutin perjalanan?
    {r}: Ayp sekarang aja
    {k}: ....
    {p}: Kamu kemaren keluar?
    {k}: Nggak
    {p}: [ Jelas dia keluar ]
    {r}: [ Setuju ]
    {p}: [ Lah, kok? ]
    {r}: Ayo jalan kalau gitu 
    {p}: Ayo""")
    time.sleep(3)
    print(f"\n{'[ Tengah gurun | selasa ]'}")
    print(f"""
    {r}: Ini lokasi paling berbahaya di gurun ini, ini adalah tempat kekuasaan cacing cacing pasir
    {k}: Pantes dari tadi aku rasa baunya aneh
    {p}: kalau begitu ayo kita cepet cepet keluar dari area ini
    {k}: Lihat sudah ada beberapa yang datang....!""")
    player.b = "Rei"
    player.k = kk
    player.l = cacing
    player.ja = 4
    warp()
    print(f"""
    {r}: Meski mereka kecil mereka kuat juga
    {p}: Karna itu mereka dibilang berbahaya
    {p}: Untung kita gak ketemu yang gede
    {k}: Hahahahaa, lain kali kita harus nutup mulur lu, doamu terjadi lagi sebaliknya """)
    time.sleep(3)
    player.b = "Rei"
    player.k = kk
    player.l = cacing_besar
    war()
    print(f"""
    {p}: Selesai juga
    {r}: Ayo istirahat aku capek
    {p}: Iya, kita lanjutin besok""")
    time.sleep(3)
    menu()
    print(f"\n{'[ gurun timur? | sabtu ]'}")
    print(f"""
    {p}: Kita udah sampai mana?
    {r}: Eee gak tau, kayaknya baru sampe timur
    {k}: Timur? bukannya ini di barat ya
    {r}: Tempat kayak gini emang suka bikin tersesat
    {p}: Terus gimana?
    {r}: Kita ambil jalan lurus aja, dan berharap nemu petunjuk
    {k}: Pohon itu termasuk petunjuk?
    {p}: Mana? adanya rumah disono
    {r}: Sepertinya kita masuk ke badai pasir halusinasi
    {p}: Iya hahahaha
    {k}: Liat udah gila dia, hahahhahahshaadjqdqjlo;qh24]   
    {r}: Aku harus nemuin jalan keluarnya
    {r}: Sebelum kedua orang dongo ini jadi gila
    {p}: Ayo lari aja
    {r}: Ya ayo, cepetan....""")
    time.sleep(3)
    b = f"{'Bandit':<10}"
    print(f"\n{'[ Gurun barat | sabtu ]'}")
    print(f"""
    {r}: selesai juga
    {p}: Iya, gak sesulit itu ternyata
    {r}: ada bandit
    {p}: Bahaya?
    {r}: Gak kalau kita ikutin apa yang dia mau
    {b}: hey beri kami 10000Rp dan kalian selamat
    {p}: Gak punya kalo sebanyak itu, ini ada kucing kamu mau?
    {k}: Woy
    {b}: Gak, kalau gita kita akan ambil peralatan mu dan semua sisa uang mu
    {r}: Tch """)
    time.sleep(3)
    player.b = "Rei"
    player.k = kk
    player.l = bandit_gurun
    player.ja = 2
    warp()
    player.l = bandit_boss
    war()
    print(f"""
    {r}: Ayo kabur, sebelum timnya dateng lagi
    {p}: Iya ayo """)
    time.sleep(3)
    if apaan is not None:
        print(f"\n{'[ Gurun Timur | senin ]'}")
        print(f"""
        {p}: Itu bukannya jack ya?
        {p}: Samperin yuk
        {r}: y
        {p}: Jack mau kemana kamu
        {j}: Jangan ganggu aku dulu
        {p}: Aku cuman takut kamu masuk ke badai pasir lagi, hahaha
        {k}: Yang kemarin kalian temui di tengah badai pasir itu dia?
        {p}: Iya, kamu gak liat ya
        {k}: Tau gak kemaren aku liat ada mayat dideket dia kemarin
        {j}: ???
        {r}: Hey hey hey
        {p}: Jack?
        """)
        while True:
            ttt = input("kemungkina menang 40%: [ A.Lawan ] [ B.Kabur ] : ")
            if ttt == "A": 
                time.sleep(3)
                player.b = "Rei"
                player.k = kk
                player.l = jack
                war()
                player_skill.append(shot)
                break
            elif ttt == "b":
                break
            else:
                continue
    print(f"\n{'[ Gurun Timur | selasa ]'}")
    print(f"""
    {p}: Lihat itu, ada temple
    {r}: Itu adalah tujuan kita ayo kesana
    {k}: Akhirnya
    {p}: Kalau begitu ayo masuk..
    {k}: Y """)
    time.sleep(3)
    print(f"\n{'[ Tample | senin ]'}")
    print(f"""
    {p}: Lihat kita disambut
    {k}: Gak ramah amat sambutannya""")
    time.sleep(3)
    player.b = "Rei"
    player.k = kk
    player.l = guardian
    player.ja = 2
    warp()
    menu()
    print(f"\n{'[ Tample | selassa ]'}")
    print(f"""
    {p}: Rei tau gak kalo aku berasal dari dunia lain
    {r}: Udah tau, dari awal kamu dateng aku udah nebak
    {p}: Setelah semua ini selesai, aku ingin kembali ke dunia asal ku
    {k}: ....
    {k}: Woy gw juga disini
    {p}: Iya tapi aku bukan messiah
    {r}: Iya iya
    {p}: Mau gak ikut ke dunia ku?
    {r}: Makasih tapi gak, aku punya peran penting di dunia ini
    {r}: orang yang mau kita temui nanti itu adalah kenalan ku
    {p}: wow, kamu intel?
    {r}: Bukan lah
    {k}: Udah dulu ngobrolnya, ada uler super gede didepan kita!!""")
    player.b = "Rei"
    player.k = kk
    player.l = snake_god
    war()
    print(f"""
    {k}: Ayo lanjut gw liat cahaya di nono, dan ada bau yang enak
    {p}: Gila kota ini 3x lebih baik dari kerajaan kita
    {r}: ayo masuk, kita juga perlu tau ada dimana si dawn """)
    time.sleep(3)
    print(f"\n{'[ Kota asing | selassa ]'}")
    print(f"""
    {p}: Ayo kita berpencar, cari informasi 
    {r}: Ide bagus
    {k}: Gw akan ke timur [ gatau sih ]
    {r}: Aku ke barat
    {p}: Oke.""")
    time.sleep(3)
    o = f"{'Orang':<10}"
    print(f"""
    {p}: pak ini kota yang dipimpin sama raja dawn, kan ya?
    {o}: Iy sir, kamu pengusup kaah?
    {p}: Enggak
    {o}: Gpp kok, pengusup yang dateng kesini juga biasanya gak mau keluar, karna emang tempat ini super bagus
    {o}: Di luar pada bilang raja kita itu buruk dll, sebenernya mah sebagus ini
    {p}: Terus kenapa dia diem aja?
    {o}: Raja kerajaan mu itu orang jahat dia menahan dawn agar tidak keluar
    {o}: Meskipun dawn bisa menang tapi dawn menolak perang
    {p}: Wow, sehebat itu kah dia
    {o}: Iya hampir semua fasilitas di negara ini gratis, ditanggung oleh pajak orang orang kaya
    {p}: Kamu tau si dawn ini dmn?
    {o}: Dia ada di kerajaan tengah kota ini
    {p}: Oke pak makasih.
    {p}: Aku harus temui mereka lagi.""")
    time.sleep(3)
    print(f"""
    {p}: Sampe juga kamu {kk}
    {k}: Si Rei belom dateng?
    {p}: Belom, mau nunggu dia dulu?
    {k}: Iy, lebih baik gitu""")
    time.sleep(3)
    print(f"""
    {p}: Mana Rei, udah malem banget
    {k}: Aku akan cari penginapan, kamu cari Rei oke""")
    time.sleep(3)
    print(f"""
    {p}: Banyak yang bilang Rei pergi ke Kerajaan dawn
    {k}: Kalau begitu besok ayo kita kesana
    {p}: Iya """)
    time.sleep(3)
    dw = f"{'Raja dawn':<10}"
    pn = f"{'Penjaga':<10}"
    print(f"\n{'[ Kerajaan dawn? | selassa ]'}")
    print(f"""
    {k}: Boleh kah kita masuk?
    {pn}: Ada urusan apaan?
    {p}: Pengen benerin ac
    {pn}: Oh oke, masuk
    {k}: Pinter juga
    {p}: Hehe
    {k}: Itu si Rei
    {p}: Reeii!!
    {r}: Ah, itu mereka rekan perjalanan ku
    {dw}: oh jadi kalian yang ngebunuh penjaga tample ku
    {p}: ....
    {p}: Rei?
    {r}: Raja dawn ini Bapak ku, jadi santai aja
    {dw}: Ayo duduk dulu
    {r}: Jadi tanyain apa aja yang kamu mau tahu
    {p}: Kenapa gak kasiih tau kamu sedeket itu sama Raja
    {r}: Biar kalian kaget
    {k}: Entar tujuan aku ikut kalian apa dah? [ dev lupa mikirin ]
    {k}: Aku tinggak sini aja yak
    {dw}: Oke, jadi guardian ku ya
    {k}: Y
    {p}: Gimana cara balik ke dunia asal ku?
    {dw}: Gak bisa, dunia ini adalah dunia asal mu yang berubah, karna keinginan mu sendiri
    {p}: Kenapa pilihan ku bisa mengubah ini?
    {dw}: Semua hal di dunia ini tercipta kerena pikiran kita sendiri 
    {p}: ....
    {dw}: Tau gak kalau semua yang kita lakuin itu udah ada yang nentuin
    {r}: Sorry ya, orang keseringan belajar filsafat emang gitu, besok jadi socrates dia
    {p}: Jadi aku gak bisa balik?
    {dw}: Balik? Sejak awal kamu itu tidak pernah pergi
    {dw}: Satu satunya cara untuk mengembalikan dunia seperti yang kamu mau hanya dengan MATI.
    {dw}: Pilih pilihan mu sendiri
    {r}: Bukan itu yang kita sepakati
    {dw}: Dia yang berhak memutuskan """)
    end = input(f"[ A.Tetap tinggal ] [ B.Pergi ] : ")
    while True:
        if end == "A":
            print(f"""
    Kamu memilih tinggah.
    Nantu kelak kamu akan meneruskan tahta raja dawn, Hidup mu bahagia dengan Rei, dan teman baikmu {kk}, meski kadang
    masih memikirkan tempat asal mu.




    Tamat
    """)
            break
        elif end == "B": 
            print(F"""
    Kamu memilih mati dan kembali ketempat asal mu
    Rei dan {kk} sangat sedih karna pilihan mu, Rei sangat marah kepada ayahnya meskipun ayahnya benar. Rei menerima tawaran mu
    pergi karna dia tertarik kepada mu yang polos pada saat itu. semua rencana Rei yang pintar hancur karna pilihan mu. meski begitu itu bukan salah mu.




    Tamat
    """)
            break