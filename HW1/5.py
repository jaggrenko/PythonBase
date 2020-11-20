fail_inp_msg = 'Вы ввели неверное значение, введите данные повторно!'
company_works_msg = 'Фирма работает'

while True:
    user_proceeds = input('Уважаемый пользователь, введите сумму выручки: ')
    user_cost = input('Уважаемый пользователь, введите сумму издержек: ')

    if user_proceeds.isdigit() and user_cost.isdigit():  # проверка на положительное целое
        proceeds_int = int(user_proceeds)
        cost_int = int(user_cost)
        if proceeds_int < cost_int:  # работа в убыток
            print(f'{company_works_msg} в убыток')
            break
        elif proceeds_int > cost_int:  # рентабельность > 0
            print(f'{company_works_msg} в прибыль c рентабельностью '
                  f'{(proceeds_int - cost_int) / proceeds_int * 100}%')  # рентабельность в %
            user_staff = input('Какова штатная численность фирмы? ')
            if user_staff.isdigit() and int(user_staff) > 0:
                print(f'Удельная прибыль на одного сотрудника составляет: '
                      f'{(proceeds_int - cost_int) / int(user_staff)} у.е.')  # удельная прибыль от штата
            else:
                print(fail_inp_msg)
                continue  # нашапесняхорошаначинайсначала :)
            break
        else:
            print(f'{company_works_msg} с нулевой рентабельностью')  # когда работа за идею
            break
    else:
        print(fail_inp_msg)
