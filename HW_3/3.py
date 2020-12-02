from my_numbers import str_conv_num


def my_func(arg_1, arg_2, arg_3):
    return max(arg_1, arg_2) + max(arg_2, arg_3)


flag_exit = False

while not flag_exit:
    tmp_lst = []
    for i in range(1, 4):
        status, val = str_conv_num(input(f'Введите число #{i}: '))
        if status:
            tmp_lst.append(val)
        else:
            print('Вы ввели число в неверном формате!')
            break
    else:
        flag_exit = True
else:
    print(my_func(tmp_lst[0], tmp_lst[1], tmp_lst[2]))
