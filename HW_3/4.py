from my_numbers import str_conv_num, negative_degree_easy_mode, negative_degree_cycle_mode, negative_degree_recursive

BASE_MSG = 'Введите действительное положительное число: '
DEGREE_MSG = 'Введите целое отрицательное число: '
ERROR_MSG = 'Неверный формат переменных!'

flag_exit = False

while not flag_exit:
    status_x, val_x = str_conv_num(input(BASE_MSG))
    status_y, val_y = str_conv_num(input(DEGREE_MSG))

    if status_x & status_y and val_x > 0 and val_y < 0:
        val_y = int(abs(val_y))
        flag_exit = True
    else:
        print(ERROR_MSG)
        continue
else:
    print(negative_degree_easy_mode(val_x, val_y))
    print(negative_degree_cycle_mode(val_x, val_y))
    print(negative_degree_recursive(val_x, val_y))
