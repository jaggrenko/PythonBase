INPUT_REQ = 'Введите информацию о товаре'
ERROR_MSG = 'Вы ввели неверное значение!'

analyze_lst = {'название': [], 'цена': [], 'количество': [], 'ед.изм': []}
goods_struct = []
user_exit = False

print('Для выхода из программы введите *')

while not user_exit:
    print(INPUT_REQ)
    tmp_dict = {}

    for i, cat in enumerate(analyze_lst.keys(), 1):
        val = input(f'{cat}: ')
        if val == '*':
            tmp_dict.clear()  # убираем мусор
            user_exit = True
            print('\nРезультат:\n[') # [ <-- жертва ТЗ
            break
        elif i >> 1 == 1 and val.isdigit():
            tmp_dict[cat] = int(val)
        elif i >> 1 != 1 and val:
            tmp_dict[cat] = val
        else:
            print(ERROR_MSG)
            tmp_dict.clear()  # убираем мусор
            break

    if len(tmp_dict):
        goods_struct.append(tuple([len(goods_struct) + 1, tmp_dict.copy()]))
        [analyze_lst[key].append(tmp_dict[key]) for key in analyze_lst.keys()]
else:
    print(*goods_struct, sep=',\n', end='\n\n]\n\n{\n')
    #print(*analyze_lst.items(), sep=',\n', end='\n\n}') # питонично :)
    for i, key in enumerate(analyze_lst, 1): # <-- еще одна жертва ТЗ
        [print(f'"{key}": {analyze_lst[key]},', end='\n') if i < len(analyze_lst)
         else print(f'"{key}": {analyze_lst[key]}', end='\n\n}')]
