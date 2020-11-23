while True:
    user_current = input('Уважаемый пользователь, введите текущий результат спортсмена:')
    user_target = input('Уважаемый пользователь, введите желаемый результат спортсмена:')

    if user_current.isdigit() and user_target.isdigit():
        current_int = int(user_current)
        target_int = int(user_target)

        if target_int <= current_int:
            print('Мы должны улучшить результат!')
            continue
        else:
            i = 0
            while current_int < target_int:
                current_int *= 1.1
                i += 1
            else:
                print(f'Спортсмен достигнет желаемого результата {target_int} на {i} день')
        break
    else:
        print('Вы ввели неверное значение!')
