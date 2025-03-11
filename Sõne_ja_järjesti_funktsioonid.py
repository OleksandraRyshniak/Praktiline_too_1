sõne = "Hello World"
sõne_list=list(sõne)
print(sõne_list)
while True:
    print("1. Удалит индекс(индекс вводит пользователь). ")
    print("2. Печатает все элементы в списке по очереди. ")
    print("3. Переводит все буквы в списке к верхнему регистру. ")
    print("4. Переводит все буквы в списке к нижнему регистру.")
    print("5. Удаляем последний объект в списке. ")
    print("6. Копирование списка.  ")
    print("7. Расширяет список, добавляя в конец все элементы списка, которые введет пользователь. ")
    print("8. Сложение списков.  ")
    print("9. Вставляет значение, которое введет пользователь на позицию, которую также вводит пользователь. . ")
    print("10. Очищение всего списка. ")
    try:
        valik=int(input( ))
        if valik==1:
            try:
                el=int(input("Введите число: "))
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
            print(f"{f},результат - {sõne_list} ")
        elif valik==6:
            copy=sõne_list.copy()
            print(copy)
        elif valik==7:
            l=input("Введите любое слово/предложение: ")
            l_list=list(l)
            d=sõne_list.extend(l)
            print(sõne_list)
        elif valik==8:
           l_list=list(input("Введите любое значение: "))
           summ=l_list+sõne_list
           print(summ)
        elif valik==9:
            i=int(input("Введите число:"))
            k=input("Введите любую букву/слово/предложение: ")
            vastus=sõne_list.insert(i, k)
            print(sõne_list)
        elif valik==10:
            res=sõne_list.clear()
            print(sõne_list)
        else:
            print("Введите значение от 1 до 10. ")
    except:
        print("Value formaat! ")
     