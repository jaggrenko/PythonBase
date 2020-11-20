while True:
    user_input = input('Уважаемый пользователь, введите целое положительное число:')
    if user_input.isdigit():
        print(sum([int(user_input*i) for i in range(1, 4)]))
        break
    else:
        print('Вы ввели неверное значение!')
