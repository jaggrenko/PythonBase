from my_email import is_email


INPUT_REQ = 'Уважаемый пользователь,\nвведите следующие данные:'
ERROR_MSG = 'Вы ввели неверное значение!'

person_dict = {'имя': [],               # 0001
               'фамилия': [],           # 0010
               'год рождения': [],      # 0011
               'город проживания': [],  # 0100
               'e-mail': [],            # 0101
               'телефон +7': []            # 0110
               }

goods_struct = []
user_exit = False

print('Для выхода из программы введите *')

while not user_exit:
    print(INPUT_REQ)
    tmp_dict = {}

    for i, person_param in enumerate(person_dict.keys(), 1):
        val = input(f'{person_param}: ')
        if val == '*':
            tmp_dict.clear()  # убираем мусор
            user_exit = True
            print('\nРезультат:\n[')
            break
        elif i != 5 and ((i % 3 == 0 and val.isdigit())  # год рождения, номер телефона
                         or (i % 3 != 0 and val.isalpha())):  # имя, фамилия, город
            tmp_dict[person_param] = val
        elif (i == 5 and len(val) > 2) and is_email(val):  # минимальная длина e-mail 3
            tmp_dict[person_param] = val
        else:
            print(ERROR_MSG)
            tmp_dict.clear()  # убираем мусор
            break

    if len(tmp_dict):
        [person_dict[key].append(tmp_dict[key]) for key in person_dict.keys()]
        user_exit = True
else:
    print(f'{*person_dict.items(),}')  # питонично :)
