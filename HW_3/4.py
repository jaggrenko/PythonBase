from my_numbers import str_conv_num, negative_degree_easy_mode, negative_degree_cycle_mode, negative_degree_recursive

flag_exit = False

while not flag_exit:
    status_x, val_x = str_conv_num(input('Введите действительное положительное число: '))
    status_y, val_y = str_conv_num(input('Введите целое отрицательное число: '))

    if status_x & status_y and val_x > 0 and val_y < 0:
        val_y = int(abs(val_y))
        flag_exit = True
    else:
        print('Неверный формат переменных!')
        continue
else:
    print(negative_degree_easy_mode(val_x, -val_y))
    print(negative_degree_cycle_mode(val_x, val_y))
    print(negative_degree_recursive(val_x, val_y))
