sõne = "Hello World"
sõne_list=list(sõne)
print(sõne_list)
while True:
    print("1. Kustutab indeksi (kasutaja sisestab indeksi). ")
    print("2. Prindib kõik elemendid järjestikku loendis. ")
    print("3. Teisendab kõik tähed loendis suurtähtedeks. ")
    print("4. Teisendab kõik tähed loendis väiketähtedeks. ")
    print("5. Kustutame viimase objekti loendist. ")
    print("6. Loendi kopeerimine. ")
    print("7. Laiendab loendit, lisades lõppu kõik elemendid, mille kasutaja sisestab. ")
    print("8. Loendite liitmine. ")
    print("9. Konkreetse elemendi muutmine loendis (kasutaja sisestab indeksi). ")
    print("10. Kogu loendi tühjendamine. ")
    try:
        valik=int(input( ))
        if valik==1:
            try:
                el=int(input("Sisesta number: "))
                del sõne_list[el] 
                print(sõne_list)
            except:
                print("Vale formaat!")
        elif valik==2:
            for x in sõne_list:
                print(x)
        elif valik==3:
            b=[x.upper() for x in sõne_list]
            print(b)
        elif valik==4:
            c=[x.lower() for x in sõne_list]
            print(c)
        elif valik==5:
            f=sõne_list.pop()
            print(f"{f},tulemus - {sõne_list} ")
        elif valik==6:
            copy=sõne_list.copy()
            print(copy)
        elif valik==7:
            while 1:
                try:
                    l=input("Sisesta ükskõik milline sõna/lausung: ")
                    if l.isalpha():break
                except:
                    print("Vale formaat!")
            l_list=list(l)
            d=sõne_list.extend(l)
            print(sõne_list)
        elif valik==8:
            while 1:
                try:
                    k_list=list(input("Sisesta ükskõik milline väärtus: "))
                    if k_list.isalpha(): break
                except:
                    print("Vale formaat!")
            summ=k_list+sõne_list
            print(summ)
        elif valik==9:
            while True:
                try:
                    i=int(input("Sisesta number: "))
                    break
                except:
                    print("Vale formaat!")
            while 1:
                try:
                    k=input("Sisesta ükskõik milline täht/sõna/lausung: ")
                    if k.isalpha(): break
                except:
                    print("Vale formaat!")
            sõne_list[i]=k
            print(sõne_list)
        elif valik==10:
            res=sõne_list.clear()
            print(sõne_list)
        else:
            print("Sisesta väärtus vahemikus 1 kuni 10. ")
    except:
        print("Value formaat! ")
     