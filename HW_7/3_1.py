class Cell:
    def __new__(cls, nucleus):
        if isinstance(nucleus, int) and nucleus > 0:
            instance = object.__new__(cls)
            instance.nucleus = nucleus
            return instance
        else:
            return None

    def __make_order(self):
        head, tail = divmod(self.nucleus, 5)  # количество ячеек кратно 5
        return f'{"{}{}".format("*****", chr(10)) * head}{"*" * tail}\n'

    def __add__(self, other):
        return f'method ADD: new {Cell(self.nucleus + other.nucleus)}'

    def __sub__(self, other):
        return f'method SUB: new {Cell(self.nucleus - other.nucleus)}'

    def __mul__(self, other):
        return f'method MUL: new {Cell(self.nucleus * other.nucleus)}'

    def __truediv__(self, other):
        return f'method DIV: new {Cell(self.nucleus // other.nucleus)}'

    def __str__(self):
        return f'cell of nucleases x{self.nucleus}\n{self.__make_order()}'

    def __enter__(self):
        return self

    def __exit__(self, type_of, value, traceback):
        print(f'--> родительский объект уничтожен: {self}')


try:
    with Cell(8) as cell_0, Cell(10) as cell_1:
        print(cell_0 + cell_1)
        print(cell_1 - cell_0)
        print(cell_0 * cell_1)
        print(cell_1 / cell_0)
except AttributeError:
    print('Конструктору передан неверный аргумент.\nНеобходимо целое число > 0')
except TypeError:
    print('Конструктору передан неверный тип аргумента.\nНеобходимо целое число > 0')
