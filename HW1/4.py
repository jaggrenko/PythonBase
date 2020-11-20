while True:
    user_input = input('Уважаемый пользователь, введите целое положительное число:')
    if user_input.isdigit():
        print(max(list(user_input)))
        break
    else:
        print('Вы ввели неверное значение!')
