sõne = "Hello World"
sõne_list=list(sõne)
print(sõne_list)
while True:
    print("1. Сложение списков. ")
    print("2. Повторение списка. ")
    print("3. Длина списка. ")
    print("4. Сборка строки из списка с разделителем S.")
    valik=int(input( ))
    if valik==1:
        y_list=list(input("Введите любое слово "))
        x=sõne_list + y_list
        print(x)
    elif valik==2:
        kogus=int(input("Введите число"))
        a=sõne_list * kogus
        print(a)
    elif valik==3:
        b=len(sõne_list)
        print(b)
    elif valik==4:
        s=" "
        c=s.join(sõne_list)
        print(c)