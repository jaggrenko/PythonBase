from my_file_functions import iterable_to_f


translate_dict = {'1': 'Один',
                  '2': 'Два',
                  '3': 'Три',
                  '4': 'Четыре'
                  }

tmp_dict = {}
if type(iterable_to_f(reverse=True, f_name='eng_nums.txt', f_mode='r',
                      func=lambda _, y: tmp_dict.update({str(y.split(" - ")[:-1]): y.split(' - ')[1:]}))) is bool:
    z = [f'{translate_dict[value[0][:-1]]} — {value[0][:-1]}' for value in tmp_dict.values()]
    if type(iterable_to_f(f_name='rus_nums.txt', f_mode='w', iter_obj=z,
                          func=lambda f_obj, el: f_obj.writelines(f'{el}\n'))) is not bool:
        print('Error')
else:
    print('Error')
