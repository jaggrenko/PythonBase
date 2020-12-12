from my_numbers import str_conv_num


"""
sum_lst(list): list as argument is checked if it consists of numbers
dummy - any key to set dummy_flag True
returns boolean 'dummy_flag' and sum of list elements
"""


def sum_lst(lst):
    lst_sum = 0
    dummy_flag = False
    dummy = '*'
    if dummy in lst and (lst.index(dummy) + 1) == len(lst):
        lst = lst[:lst.index(dummy)]
        dummy_flag = True

    for el in lst:
        status, tmp = str_conv_num(el)
        if not status:
            lst.clear()
            return False, 0
    else:
        lst_sum += sum(map(int, lst))

    return dummy_flag, lst_sum


REQUEST_MSG = 'Введите числа через пробел: '
INFO_MSG = 'Уважаемый пользователь!\nДанная программа расчитывает сумму чисел,\n' \
           'введеных через пробел.\nДля выхода из программы введите: * '

flag_exit = False
output_sum = 0
print(INFO_MSG)

while not flag_exit:
    user_lst_num = input(REQUEST_MSG).split()
    flag_exit, func_sum = sum_lst(user_lst_num)
    output_sum += func_sum
    print(f'Сумма: {output_sum}')
else:
    print(f'Выход')
