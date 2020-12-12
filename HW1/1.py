user_inputs = []
REQUEST_COUNT = 3

for i in range(REQUEST_COUNT):
    user_input = input('Уважаемый пользователь, введите число или строку')
    user_inputs.append(user_input)

print('Вы ввели следующие значения:')
[print(val) for val in user_inputs]
