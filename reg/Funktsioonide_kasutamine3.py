from Mymodul3 import *


praegune_kasutaja = None

while True:
    print(login_password_list)
    print(praegune_kasutaja)
    print("tehke valiku: ")
    print("1.Registreerimine")
    print("2.Sisselogimine")
    print("3.Vahetada kasutaja logini")
    print("4.taastada parooli")
    print("5.väljada")

    # kusi valikku
    valik = input("tee valikku: ")
    if valik == "1":
        if praegune_kasutaja is not None:
            print("Te juba olete")
            continue
        login = input("looge sinu loginni: ")
        parool = input("looge sinu parooli: ")
        index = register(login, parool)
        praegune_kasutaja = index
    elif valik == "2":
        if praegune_kasutaja is not None:
            print("Te juba olete")
            continue
        kasutajanimi = input("sisesta sinu loginni: ")
        parool = input("sisesta sinu paroooli:")
        kasutaja_indeksi = authorize(kasutajanimi, parool)
        praegune_kasutaja = kasutaja_indeksi
    elif valik == "3":
        if praegune_kasutaja is None:
            print("pead sisselogima")
            continue
        uus_login = input("sisesta sinu uus logiini: ")
        change_login(praegune_kasutaja, uus_login)
    elif valik == "4":
        if praegune_kasutaja is not None:
            print("Te juba olete")
            continue
        nimi = input("sisesta sinu nimi: ")
        if nimi not in login_password_list[0]:
            print("ei ole kasutajat selle nimega!")
            continue

        parool = recover_password(login_password_list[0].index(nimi))
        vana_parool = input("sisesta sinu vana parooli, mis saadakse e-postisse: ")
        if vana_parool != parool:
            print("vale parool!")
            continue
        praegune_kasutaja = login_password_list[0].index(nimi)

    elif valik == "5":
        praegune_kasutaja = None
