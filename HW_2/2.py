list_val = []
result = []
input_req = 'Уважаемый пользователь, введите необходимую длину списка (число > 1): '

list_len = input(input_req)

while True:
    if list_len.isdigit() and int(list_len) > 1:
        # в цикле наполняем список любыми значениями
        [list_val.append(input(f'Введите значение #{i+1}: ')) for i in range(int(list_len))]
        print(f'Исходный список: {*list_val,}')
        # while len(list_val) < int(list_len):  # если не нужен индекс
        #     list_val.append(input(f'Введите значение: '))
        # else:
        #     print(f'Исходный список: {*list_val,}')

        # вариант_1 (питоничный)
        for index in range(0, len(list_val) - 1, 2):
            list_val[index], list_val[index + 1] = list_val[index + 1], list_val[index]
            result.extend(list_val[index:index + 2])
        # вариант_1 (непитоничный)_ PyDzen: простое лучше сложного
        # list_res = list(zip(list(filter(lambda x: list_val.index(x) % 2, list_val)),
        #                    list(filter(lambda x: not list_val.index(x) % 2, list_val))))
        # [[result.append(i) for i in ii] for ii in list_res]
        if int(list_len) & 1:  # проверка на нечетность
            result.append(list_val[-1])
        print(f'Конечный список: {*result,}')
        break
    else:
        print('Вы ввели неверное значение!')
        list_len = input(input_req)
        continue
