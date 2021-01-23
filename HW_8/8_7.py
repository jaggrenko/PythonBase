from my_func import str_conv_num as scn


class ComplexMethods(object):
    def __new__(cls, u_complex):
        try:
            _u_complex = complex(u_complex)
        except:
            _status, _u_complex = scn(str(u_complex))
            if _status:
                _u_complex = complex(_u_complex)
            else:
                raise TypeError(f'Ошибка: неверно задан тип переменной --> {u_complex}')

        instance = object.__new__(cls)
        instance.u_complex = _u_complex
        return instance

    def __add__(self, other):
        return self.u_complex + other.u_complex

    def __mul__(self, other):
        return self.u_complex * other.u_complex

    def __str__(self):
        return str(self.u_complex)


try:
    cm_0 = ComplexMethods(2 + 3j)
    cm_1 = ComplexMethods('-1')
    print(cm_0 + cm_1)
    print(cm_0 * cm_1)
except TypeError as err:
    print(f'{err}')
