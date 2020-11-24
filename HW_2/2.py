list_len = input('Уважаемый пользователь, введите необходимую длину списка: ')
list_val = []
list_res = []

if list_len.isdigit():
    while len(list_val) < int(list_len):
        list_val.append(input('Введите значение: '))
    else:
        print(f'Исходный список: {list_val}')

    list_res = list(zip(list(filter(lambda x: list_val.index(x) % 2, list_val)),
                        list(filter(lambda x: not list_val.index(x) % 2, list_val))))
    print(list_res) if not int(list_len) % 2 else print(list_res.append(list_val[len(list_val)]))
