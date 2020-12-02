from my_numbers import str_conv_num


def div_numbers(arg_1, arg_2):
    flag_1, val_1 = str_conv_num(arg_1)
    flag_2, val_2 = str_conv_num(arg_2)

    if (flag_1 and flag_2) and val_2 != 0:
        return '%.2f' % (val_1 / val_2)
    elif val_2 == 0:
        return 'Деление на 0!'
    else:
        return 'Неверный формат!'


print(div_numbers(input('Введите делимое число: '), input('Введите делитель: ')))
