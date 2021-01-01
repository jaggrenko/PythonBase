from my_file_functions import iterable_to_f

tmp_dict = {}
dict_key = ''
dict_val = 0
lst_delim = '('


tmp_lst = []
if type(iterable_to_f(reverse=True, f_name='stud_plan.txt', f_mode='r',
                      func=lambda _, el: tmp_lst.append(el.split()))) is bool:

    z = [(el[:el.find(lst_delim)]) for els in tmp_lst for el in els if lst_delim in el or el[:-1].isalpha()]
    for el in z:
        if el.isalpha():
            dict_key, dict_val = el, 0
        else:
            dict_val += int(el)
            tmp_dict[dict_key] = dict_val
    else:
        print({**tmp_dict, })
else:
    print('Error')
