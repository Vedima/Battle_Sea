class Ship:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y


class Ship_1P(Ship): # Делаем контур вокруг корабля с 1 палубой на 1 клетку
    def pointsAround(self, x, y, matrix):
        if (x < 5):
            matrix[x + 1][y] = '-'
        if (x > 0):
            matrix[x - 1][y] = '-'
        if (x < 5) and (y < 5):
            matrix[x + 1][y + 1] = '-'
        if (x > 0) and (y > 0):
            matrix[x - 1][y - 1] = '-'
        if (x < 5) and (y > 0):
            matrix[x + 1][y - 1] = '-'
        if (x > 0) and (y < 5):
            matrix[x - 1][y + 1] = '-'
        if (y < 5):
            matrix[x][y + 1] = '-'
        if (y > 0):
            matrix[x][y - 1] = '-'

    def putToField(self, matrix): # Отмечаем корабли на поле
        matrix[self.x][self.y] = '#'
        self.pointsAround(self.x, self.y, matrix)


class Ship_2P(Ship):
    def __init__(self, size, x, y, x1, y1):
        self.size = size
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def pointsAround(self, x, y, x1, y1, matrix):  # Делаем контур вокруг корабля с 2 палубами на 1 клетку
        if (x < 5):
            matrix[x + 1][y] = '-'
        if (x > 0):
            matrix[x - 1][y] = '-'
        if (x < 5) and (y < 5):
            matrix[x + 1][y + 1] = '-'
        if (x > 0) and (y > 0):
            matrix[x - 1][y - 1] = '-'
        if (x < 5) and (y > 0):
            matrix[x + 1][y - 1] = '-'
        if (x > 0) and (y < 5):
            matrix[x - 1][y + 1] = '-'
        if (y < 5):
            matrix[x][y + 1] = '-'
        if (y > 0):
            matrix[x][y - 1] = '-'
        if (x1 < 5):
            matrix[x1 + 1][y1] = '-'
        if (x1 > 0):
            matrix[x1 - 1][y1] = '-'
        if (x1 < 5) and (y1 < 5):
            matrix[x1 + 1][y1 + 1] = '-'
        if (x1 > 0) and (y1 > 0):
            matrix[x1 - 1][y1 - 1] = '-'
        if (x1 < 5) and (y1 > 0):
            matrix[x1 + 1][y1 - 1] = '-'
        if (x1 > 0) and (y1 < 5):
            matrix[x1 - 1][y1 + 1] = '-'
        if (y1 < 5):
            matrix[x1][y1 + 1] = '-'
        if (y1 > 0):
            matrix[x1][y1 - 1] = '-'

    def putToField(self, matrix): # Отмечаем корабли на поле
        self.pointsAround(self.x, self.y, self.x1, self.y1, matrix)
        matrix[self.x][self.y] = '#'
        matrix[self.x1][self.y1] = '#'

class Ship_3P(Ship):
    def __init__(self, size, x, y, x1, y1):
        self.size = size
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def pointsAround(self, x, y, x1, y1, matrix): # Делаем контур вокруг корабля с 1 палубой на 1 клетку
        if (x < 5):
            matrix[x + 1][y] = '-'
        if (x > 0):
            matrix[x - 1][y] = '-'
        if (x < 5) and (y < 5):
            matrix[x + 1][y + 1] = '-'
        if (x > 0) and (y > 0):
            matrix[x - 1][y - 1] = '-'
        if (x < 5) and (y > 0):
            matrix[x + 1][y - 1] = '-'
        if (x > 0) and (y < 5):
            matrix[x - 1][y + 1] = '-'
        if (y < 5):
            matrix[x][y + 1] = '-'
        if (y > 0):
            matrix[x][y - 1] = '-'
        if (x1 < 5):
            matrix[x1 + 1][y1] = '-'
        if (x1 > 0):
            matrix[x1 - 1][y1] = '-'
        if (x1 < 5) and (y1 < 5):
            matrix[x1 + 1][y1 + 1] = '-'
        if (x1 > 0) and (y1 > 0):
            matrix[x1 - 1][y1 - 1] = '-'
        if (x1 < 5) and (y1 > 0):
            matrix[x1 + 1][y1 - 1] = '-'
        if (x1 > 0) and (y1 < 5):
            matrix[x1 - 1][y1 + 1] = '-'
        if (y1 < 5):
            matrix[x1][y1 + 1] = '-'
        if (y1 > 0):
            matrix[x1][y1 - 1] = '-'

    def putToField(self, matrix): # Ищем промежуточную точку для 3-ёх палубного и отмечаем корабль на поле
        self.pointsAround(self.x, self.y, self.x1, self.y1, matrix)
        matrix[self.x][self.y] = '#'
        matrix[self.x1][self.y1] = '#'
        self.x2 = (self.x + self.x1) // 2
        self.y2 = (self.y + self.y1) // 2
        matrix[self.x2][self.y2] = '#'

