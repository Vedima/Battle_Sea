from ship import Ship, Ship_1P, Ship_2P, Ship_3P
class Field:
    matrix = [
        ['~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~'],
        ['~', '~', '~', '~', '~', '~']
    ]
    count1 = 0
    count2 = 0
    count3 = 0
    ships_list = []
    def __init__(self, name):
        self.name = name

    def clear(self):    # Очищаем данные и перезапускаем в случае невозможной расстановки кораблей
        self.matrix = [['~'] * 6 for i in range(6)]
        self.ships_list.clear()
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0

    def checkFreeCells(self): # Проверяем ячейки на возможность внесения данных
        for row in self.matrix:
            for cell in row:
                if cell == "~":
                    return True
        return False

    def check2pShip(self ,x1 ,y1 ,x2 ,y2): # Проверяем правильность введенных данных для 2-х палубного
        if (0 <= x1 <= 6) and (0 <= y1 <= 5) and (0 <= x2 <= 5) and (0 <= y2 <= 5):
            if ((x2 == x1 + 1 or x2 == x1 - 1) and y1 == y2) or ((y2 == y1 + 1 or y2 == y1 - 1) and x1 == x2):
                return True
            else:
                return False
        else:
            return False

    def check3pShip(self ,x1 ,y1 ,x2 ,y2): # Проверяем правильность введенных данных для 3-х палубного
        if (0 <= x1 <= 5) and (0 <= y1 <= 5) and (0 <= x2 <= 5) and (0 <= y2 <= 5):
            if ((x2 == x1 + 2 or x2 == x1 - 2) and y1 == y2) or ((y2 == y1 + 2 or y2 == y1 - 2) and x1 == x2):
                return True
            else:
                return False
        else:
            return False

    def checkPoint(self, x, y): # Проверяем занята ли точка для добавления корабля
        if self.matrix[x][y] != '~':
            return False
        else:
            return True

    def add_ship(self, lData): # Добавляем корабль на поле

        if len(lData) < 3:
            return False
        if lData[0] == 1:
            if self.count1 >= 4:
                return False
            if (0 <= lData[1] <= 5) and (0 <= lData[2] <= 5) and self.checkPoint(lData[1], lData[2]):
                cur_ship = Ship_1P(1, lData[1], lData[2])
                self.count1 = self.count1 + 1
            else:
                return False
        elif lData[0] == 2:
            if self.count2 >= 2:
                return False
            if (len(lData) >= 5):
                if self.check2pShip(lData[1], lData[2], lData[3], lData[4]) and self.checkPoint(lData[1], lData
                    [2]) and self.checkPoint(lData[3], lData[4]):
                    cur_ship = Ship_2P(2, lData[1], lData[2], lData[3], lData[4])
                    self.count2 = self.count2 + 1
                else:
                    return False
            else:
                return False

        elif lData[0] == 3:
            if self.count3 >= 1:
                return False
            if (len(lData) >= 5):
                if self.check3pShip(lData[1], lData[2], lData[3], lData[4]) and self.checkPoint(lData[1], lData[2]) \
                    and self.checkPoint(lData[3], lData[4]):
                    cur_ship = Ship_3P(3, lData[1], lData[2], lData[3], lData[4])
                    self.count3 = self.count3 + 1
                else:
                    return False
            else:
                return False
        else:
            return False
        self.ships_list.append(cur_ship)
        cur_ship.putToField(self.matrix)
        return True

    def check_count(self): # Проверка для цикла while. Ждем пока наберется необходимое количество кораблей
        if self.count1 == 4 and self.count2 == 2 and self.count3 == 1:
            return False
        return True

    def print(self, hideData=0): # Печатаем поле
        print(f'Field of {self.name}')
        print('  0 1 2 3 4 5')
        for i in range(6):
            if hideData:
                hiddenList = list(self.matrix[i])
                for j in range(6):
                    if hiddenList[j]=="#":
                        hiddenList[j] = "~"
                    if hiddenList[j] == "-":
                        hiddenList[j] = "~"
                print(i, *hiddenList)
            else:
                print(i, *self.matrix[i])

    def pointsAroundShoot(self, x, y, matrix): # Контур вокруг убитого или раненого корабля
        if  matrix[x + 1][y] == '#' or matrix[x - 1][y] == '#' \
            or matrix[x + 1][y + 1] == '#' or matrix[x - 1][y - 1] == '#' \
            or matrix[x + 1][y - 1] == '#' or matrix[x - 1][y + 1] == '#' \
            or matrix[x][y + 1] == '#' or matrix[x][y - 1] == '#':
            return True
    def shoot(self, lCoord): # Проверяем данные и делаем выстрел
        x= lCoord[0]
        y = lCoord[1]
        sps = []
        print(x, y)
        if len(lCoord) < 2:
            return 0
        if (0 > x > 5) and (0 > y > 5):
            return 0
        if self.matrix[x][y] == 'X' or self.matrix[x][y] == 'T' \
            or self.matrix[x][y] == ' ':
            return 0
        if self.matrix[x][y] == '#':
            if (x < 5):
                sps.append(self.matrix[x + 1][y])
            if (x > 0):
                sps.append(self.matrix[x - 1][y])
            if (x < 5) and (y < 5):
                sps.append(self.matrix[x + 1][y + 1])
            if (x > 0) and (y > 0):
                sps.append(self.matrix[x - 1][y - 1])
            if (x < 5) and (y > 0):
                sps.append(self.matrix[x + 1][y - 1])
            if (x > 0) and (y < 5):
                sps.append(self.matrix[x - 1][y + 1])
            if (y < 5):
                sps.append(self.matrix[x][y + 1])
            if (y > 0):
                sps.append(self.matrix[x][y - 1])
            if '#' in sps:
                self.matrix[x][y] = 'X'
                print('Попал. Стреляй дальше')
                return 1
            else:
                self.matrix[x][y] = 'X'
                if (x < 5) and self.matrix[x + 1][y] != 'X':
                    self.matrix[x + 1][y] = ' '
                if (x > 0) and self.matrix[x - 1][y] != 'X':
                    self.matrix[x - 1][y] = ' '
                if (x < 5) and (y < 5) and self.matrix[x + 1][y + 1] != 'X':
                    self.matrix[x + 1][y + 1] = ' '
                if (x > 0) and (y > 0) and self.matrix[x - 1][y - 1] != 'X':
                    self.matrix[x - 1][y - 1] = ' '
                if (x < 5) and (y > 0) and self.matrix[x + 1][y - 1] != 'X':
                    self.matrix[x + 1][y - 1] = ' '
                if (x > 0) and (y < 5) and self.matrix[x - 1][y + 1] != 'X':
                    self.matrix[x - 1][y + 1] = ' '
                if (y < 5) and self.matrix[x][y + 1] != 'X':
                    self.matrix[x][y + 1] = ' '
                if (y > 0) and self.matrix[x][y - 1] != 'X':
                    self.matrix[x][y - 1] = ' '
                print('Убит. Стреляй дальше')
                return 2
        else:
            self.matrix[x][y] = 'T'
            print('Промах')
            return 3
    def checkWinner(self): # Условие для победы
        for row in self.matrix:
            for cell in row:
                if cell == "#":
                    return False
        return True

