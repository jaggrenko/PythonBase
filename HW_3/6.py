"""
str_alpha_upper(string): words (latin alphabet) lowercase
returns boolean True and word (first letter uppercase) if input correct,
else returns boolean False and error message
"""


def str_alpha_upper(arg):
    if arg.isalpha() and arg.islower():
        for el in arg:
            if ord(el) not in range(97, 123):
                return False, 'Not latin letters'
        else:
            arg = arg.replace(arg[:1], chr(ord(arg[:1]) - 32), 1)
            return True, arg
    return False, 'Must be lowercase latin letters input'


REQUEST_MSG = 'Введите слова латиницей через пробел: '
flag_exit = False


while not flag_exit:
    user_lst_words = input(REQUEST_MSG).split()
    tmp_lst = []

    for word in user_lst_words:
        status, word = str_alpha_upper(word)
        if status:
            tmp_lst.append(word)
        else:
            print(word)
            tmp_lst.clear()
            break

    if len(tmp_lst):
        print(*tmp_lst, sep=' ')
        flag_exit = True
else:
    print('Выход')
