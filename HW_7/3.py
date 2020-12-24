# искусственный код, не более (см. 3_1)
class LEZeroException(Exception):
    def __init__(self, err_val):
        self.err_val = err_val
        self.err_msg = f'is equal or less zero'
        super().__init__(self.err_msg)

    def __str__(self):
        return f'{self.err_val} -- {self.err_msg}'


class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    @property
    def nucleus(self):
        return self.__nucleus

    @nucleus.setter
    def nucleus(self, nucleus):
        __instance_params = f'{Cell.__name__}({nucleus})'
        if type(nucleus) is int and nucleus <= 0:
            raise LEZeroException(__instance_params)
        elif type(nucleus) is not int:
            raise TypeError(f'{__instance_params} -- is not integer')
        else:
            self.__nucleus = nucleus

    def __add__(self, other):
        return f'method ADD: new {Cell(self.nucleus + other.nucleus)}'

    def __sub__(self, other):
        return f'method SUB: new {Cell(self.nucleus - other.nucleus)}'

    def __mul__(self, other):
        return f'method MUL: new {Cell(self.nucleus * other.nucleus)}'

    def __truediv__(self, other):
        return f'method DIV: new {Cell(self.nucleus // other.nucleus)}'

    def __make_order(self):
        head, tail = divmod(self.nucleus, 5)
        return f'{"{}{}".format("*****", chr(10)) * head}{"*" * tail}'

    def __str__(self):
        return f'cell of nucleases x{self.nucleus}\n{self.__make_order()}'

    def __enter__(self):
        return self

    def __exit__(self, type_of, value, traceback):
        print(f'--> родительский объект уничтожен:', self)


with Cell(3) as cell_0, Cell('8') as cell_1:
    print(cell_0 + cell_1)
    print(cell_1 - cell_0)
    print(cell_0 * cell_1)
    print(cell_1 / cell_0)
