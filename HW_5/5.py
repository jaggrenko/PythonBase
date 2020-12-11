from random import randint
from my_file_functions import iterable_to_f


int_lst = [randint(-100, 100) for _ in range(10)]
tmp_lst = []

if type(iterable_to_f(reverse=False, f_name='sum_nums.txt',
                      func=lambda x, y: x.write(f'{str(y)}\n'), iter_obj=int_lst)) is bool:
    if type(iterable_to_f(reverse=True, f_name='sum_nums.txt', f_mode='r',
                          func=lambda _, y: tmp_lst.append(int(y)))) is bool:
        print(sum(tmp_lst))
    else:
        print('Error')
else:
    print('Error')
