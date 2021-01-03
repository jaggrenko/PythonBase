from my_func import str_conv_num as scn


class NotNumber(Exception):
    def __init__(self):
        self.err_msg = 'Это не число!'

    def __str__(self):
        return self.err_msg


class NumControl:
    @staticmethod
    def u_num_ctrl(u_val):
        status, u_number = scn(u_val)
        if status:
            return u_number
        else:
            raise NotNumber


tmp_list = []
user_number = ''

while user_number != 'stop':
    user_number = input(f'Введите число: ')
    if user_number == 'stop':
        print(tmp_list)
        break
    try:
        tmp_list.append(NumControl.u_num_ctrl(user_number))
    except NotNumber as err:
        print(err)
        continue
