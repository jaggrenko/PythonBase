rating_lst = [8, 5, 5, 5, 4, 4, 3, 2, 1]
input_req = 'Введите целое положительное число: '

n = input(f'Для выхода из программы введите *\n{input_req}')

while True:
    if n == '*':
        print('Выход')
        break
    if n.isdigit():
        n = int(n)
        if n in rating_lst:
            pos = rating_lst.index(n) + rating_lst.count(n)
            rating_lst.insert(pos, n)
        else:
            rating_lst.insert(0, n)
            rating_lst.sort(reverse=True)
        print(f'Рейтинг: {*rating_lst,}')
        n = input(input_req)
    else:
        n = input(f'Вы ввели ошибочное значение!\n{input_req}')
        continue
