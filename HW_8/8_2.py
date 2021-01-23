from my_func import str_conv_num as scn


class ZeroDiv(Exception):
    def __init__(self):
        self.err_msg = 'Деление на 0!'

    def __str__(self):
        return self.err_msg


user_divider = input(f'Введите делитель: ')
status, user_divider = scn(user_divider)

if status:
    try:
        if user_divider != 0:
            tmp_val = 5 / user_divider
        else:
            raise ZeroDiv()
    except ZeroDiv as err:
        print(err)
else:
    print('Неверный тип данных!\nВведите число!')
