from my_func import str_conv_num as scn


class NotNumber(Exception):
    def __init__(self):
        self.err_msg = 'Это не число!'

    def __str__(self):
        return self.err_msg


tmp_list = []
user_number = ''

while user_number != 'stop':
    user_number = input(f'Введите число: ')
    if user_number == 'stop':
        print(tmp_list)
        break

    status, user_number = scn(user_number)
    try:
        if status:
            tmp_list.append(user_number)
        else:
            raise NotNumber()
    except NotNumber as err:
        print(err)
        continue
