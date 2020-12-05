from my_numbers import str_conv_num

REQUEST_MSG = 'Введите число #'
ERROR_MSG = 'Вы ввели число в неверном формате!'


def my_func(arg_1, arg_2, arg_3):
    lst = [arg_1, arg_2, arg_3]
    if len(set(lst)) <= 1:
        return False, 'Все элементы равны!'
    else:
        lst.remove(min(lst))
        return True, sum(lst)


flag_exit = False

while not flag_exit:
    tmp_lst = []
    for i in range(1, 4):
        status, val = str_conv_num(input(f'{REQUEST_MSG}{i}: '))
        if status:
            tmp_lst.append(val)
        else:
            print(ERROR_MSG)
            break
    else:
        status, val = my_func(tmp_lst[0], tmp_lst[1], tmp_lst[2])
        if status:
            flag_exit = True
        print(val)
