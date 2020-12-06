from itertools import count, cycle


def gen_nums_sequence(start_num=0, end_num=0):
    for el in count(start_num):
        if el > end_num:
            break
        else:
            yield el


start_gen_num = 3
exit_cycle_num = 10

[print(val) for val in gen_nums_sequence(start_gen_num, exit_cycle_num)]


tmp_lst = [1, 2, 'u', 3, '*']
counter = 0

for el in cycle(tmp_lst):
    if counter >= exit_cycle_num*len(tmp_lst):  # домножаем на длину списка
        break
    print(el)
    counter += 1
