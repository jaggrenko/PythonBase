"""
string as argument to be checked if it's number
returns boolean and float (positive or negative)
"""


def str_conv_num(arg):
    seq_set = ['.', ',', '-', '-.', '-,']

    if arg and arg not in seq_set:
        for i in arg:
            if ord(i) not in range(44, 58) or ord(i) == 47:
                return False, 0
    else:
        return False, 0

    if arg.find(seq_set[2]) < 0 or arg.find(seq_set[2]) == 0:
        if arg.count(seq_set[0]) < 2:
            if arg.count(seq_set[1]) < 2:
                if not (seq_set[0] in arg and seq_set[1] in arg):
                    if seq_set[1] in arg:
                        arg = arg.replace(seq_set[1], seq_set[0])
                    return True, float(arg)
    return False, 0


if __name__ == 'main':
    str_conv_num('')
