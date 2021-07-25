class Cell:

    def __init__(self, box):
        self.box = box

    def __add__(self, other):
        return f'Суммарное количество ячеек в клетках: {self.box + other.box}'

    def __sub__(self, other):
        if self.box - other.box > 0:
            return f'Разность ячеек: {self.box - other.box}'
        else:
            print('Разность меньше 0')

    def __mul__(self, other):
        return self.box * other.box

    def __truediv__(self, other):
        return round(self.box / other.box)

    def make_order(rows, nums):
        return '\n'.join(['*' * rows for _ in range(nums // rows)]) + '\n' + '*' * (nums % rows)

    print(make_order(4, 28))


cell_1 = Cell(28)
cell_2 = Cell(15)

print(Cell.__mul__(cell_1, cell_2))
print(Cell.__truediv__(cell_1, cell_2))
print(Cell.__add__(cell_1, cell_2))
print(Cell.__sub__(cell_1, cell_2))
