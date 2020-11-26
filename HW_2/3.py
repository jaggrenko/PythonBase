lst_seasons = [('зима', 12, 1, 2),
               ('весна', 3, 4, 5),
               ('лето', 6, 7, 8),
               ('осень', 9, 10, 11)]  # оставляем int - занимает меньший объем памяти

# dic_seasons = {12: 'зима', 1: 'зима', 2: 'зима',    # код быстрее, но занимает больше памяти
#                3: 'весна', 4: 'весна', 5: 'весна',
#                6: 'лето', 7: 'лето', 8: 'лето',
#                9: 'осень', 10: 'осень', 11: 'осень'}

dic_seas = {(1, 2, 12): "зима", (3, 4, 5): "весна", (6, 7, 8): "лето", (9, 10, 11): "лето"}

input_req = 'Уважаемый пользователь, введите месяц в виде числа (от 1 до 12): '
month = input(input_req)

while True:
    if month.isdigit() and int(month) in range(1, 13):
        [[print(f'list* {month}-й месяц - это {cortage[0]}')
          for val in cortage if val == int(month)]
            for cortage in lst_seasons]
        # print(f'dict* {month}-й месяц - это {dic_seasons[int(month)]}')
        [print(f'dict* {month}-й месяц - это {dic_seas[key]}') for key in dic_seas if int(month) in key]
        break
    else:
        print('Вы ввели неверное значение!')
        month = input(input_req)
        continue
