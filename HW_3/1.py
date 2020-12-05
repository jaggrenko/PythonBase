from my_numbers import str_conv_num

ZERO_DIV_MSG = 'Деление на 0!'
ERROR_MSG = 'Неверный формат!'
DIVIDENT_MSG = 'Введите делимое число: '
DIVIDER_MSG = 'Введите делитель: '


def div_numbers(arg_1, arg_2):
    flag_1, val_1 = str_conv_num(arg_1)
    flag_2, val_2 = str_conv_num(arg_2)

    if (flag_1 and flag_2) and val_2 != 0:
        return '%.2f' % (val_1 / val_2)
    elif val_2 == 0:
        return ZERO_DIV_MSG
    else:
        return ERROR_MSG


print(div_numbers(input(DIVIDENT_MSG), input(DIVIDER_MSG)))
