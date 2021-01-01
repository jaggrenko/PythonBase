input_req = 'Уважаемый пользователь, введите строку из нескольких слов через пробел: '
user_list = input(input_req).split()

while True:
    if len(user_list) > 1:
        [print(f'{i}: {word[:10]}') for i, word in enumerate(user_list, 1)]
        break
    else:
        user_list = input(f'Вы ввели неверное значение!\n{input_req}').split()
        continue
