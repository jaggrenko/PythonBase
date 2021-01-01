from my_file_functions import iterable_to_f


employee_dict = {}
if type(iterable_to_f(reverse=True, f_name='employee.txt', f_mode='r',
                      func=lambda _, y: employee_dict.update({str(y.split()[:-1]): y.split()[1:]}))) is bool:
    employee_20k = [name[2:-2] for name, loan in employee_dict.items() if int(loan[0]) < 20000]
    average_loan = sum(int(loan[0]) for loan in employee_dict.values())/len(employee_dict)
    print(f'Оклад < 20000:\n{employee_20k}\nСредняя зряплата сотрудников: {int(average_loan)}')
else:
    print('Error')
