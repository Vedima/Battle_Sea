import random
from field import Field

print('Расставляет корабли Игрок')
field_1 = Field('Player')
field_1.print()
while field_1.check_count():
    data = input("Введите 1, 2 или 3 (палубность) и координаты от 0 до 5: ")
    try:
        lData = list(map(int, data.split()))
    except:
        print('Введите заново')
        continue
    if field_1.add_ship(lData):
        field_1.print()
    else:
        print('Введите заново')
print('Теперь корабли расставляет компьютер ')

field_CPU = Field('CPU')
goodStand = False
while not goodStand:
    count1 = 0
    count2 = 0
    count3 = 0
    field_CPU.clear()
    while field_CPU.check_count():
        if not field_CPU.checkFreeCells() :
            print("Неудачная расстановка")
            break
        # добавляем случайный 3-x палубный
        if count3 < 1:
            d = random.randint(1, 2)
            if d == 1:
                r1 = random.randint(0, 5)
                c1 = random.randint(0, 3)
                r2 = r1
                c2 = c1 + 2
            else:
                r1 = random.randint(0, 3)
                c1 = random.randint(0, 5)
                r2 = r1 + 2
                c2 = c1
            if field_CPU.add_ship([3, r1, c1, r2, c2]):
                count3 += 1
                continue
            # добавляем случайный 2-x палубный
        if count2 < 2:
            d = random.randint(1, 2)
            if d == 1:
                r1 = random.randint(0, 5)
                c1 = random.randint(0, 4)
                r2 = r1
                c2 = c1 + 1
            else:
                r1 = random.randint(0, 4)
                c1 = random.randint(0, 5)
                r2 = r1 + 1
                c2 = c1
            if field_CPU.add_ship([2, r1, c1, r2, c2]):
                count2 += 1
                continue
            else:
                continue
            # добавляем случайный 1 палубный
        if count1 < 4:
            r1 = random.randint(0, 5)
            c1 = random.randint(0, 5)
            if field_CPU.add_ship([1, r1, c1]):
                count1 += 1
            else:
                continue
    goodStand = not field_CPU.check_count()
field_CPU.print()

curr_player = 1
while True:
    if field_CPU.checkWinner():
        print('Победитель Игрок')
        break
    if field_1.checkWinner():
        print('Победитель CPU')
        break
    field_1.print()
    field_CPU.print(1)
    if curr_player == 1:
        print('Стреляет Игрок')
        coord = input("Введите координаты от 0 до 5: ")
        try:
            lCoord = list(map(int, coord.split()))
        except:
            print('Введите заново')
            continue
        shootResult = field_CPU.shoot(lCoord)
        if shootResult == 0:
            print('Введите заново')
            continue
        elif shootResult == 1 or shootResult == 2:
            continue
        elif shootResult == 3:
            curr_player = 2
    else:
        print('Стреляет CPU')
        r = random.randint(0, 5)
        c = random.randint(0, 5)
        shootResult = field_1.shoot([r, c])
        if shootResult == 0:
            print('Введите заново')
            continue
        elif shootResult == 1 or shootResult == 2:
            continue
        else:
            curr_player = 1

print('Игра завершена')



