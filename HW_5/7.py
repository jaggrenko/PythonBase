import json

with open('cosa_nostra.txt', 'r', encoding='utf-8') as f_obj:
    tmp_dict = {}
    tmp_lst = []
    for line in f_obj:
        firma, _, proceeds, costs = line.split()
        tmp_dict[firma] = int(proceeds) - int(costs)
    else:
        z = [profit for profit in tmp_dict.values() if profit > 0]
        tmp_lst.append(tmp_dict.copy())
        tmp_dict.clear()
        tmp_dict['average_profit'] = sum(z) / len(z)
        tmp_lst.append(tmp_dict)
        with open('cosa_nostra.json', 'w') as json_obj:
            json.dump(tmp_lst, json_obj)
