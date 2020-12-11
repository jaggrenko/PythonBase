from my_file_functions import iterable_to_f


exit_flag = False
lst = []

while not exit_flag:
    user_data = input('Введите данные: ')
    if not user_data:
        exit_flag = True
    else:
        lst.append(f'{user_data}\n')
else:
    if type(iterable_to_f(f_name='test_1.txt', f_mode='a+', iter_obj=lst,
                          func=lambda f_obj, el: f_obj.writelines(el))) is bool:
        print(f'Выход')
    else:
        print('Error')

