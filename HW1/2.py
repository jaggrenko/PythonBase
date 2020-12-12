while True:
    user_input = input('Уважаемый пользователь, введите время в секундах:')
    if user_input.isdigit():
        m, s = divmod(int(user_input), 60)  # datetime.time delta
        h, m = divmod(m, 60)
        print("%02d:%02d:%02d" % (h, m, s))
        break
    else:
        print('Вы ввели неверное значение!')
