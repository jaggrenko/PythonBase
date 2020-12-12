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


"""
negative_degree_easy_mode(base, degree): float in negative degree
base as float, degree as negative number
"""


def negative_degree_easy_mode(base, degree):
    return 1/(base ** degree)


"""
negative_degree_cycle_mode(base, degree): float in negative degree
base as float, degree as int
"""


def negative_degree_cycle_mode(base, degree):
    result = base
    for i in range(1, int(degree)):
        result *= base
    return 1/result


"""
negative_degree_recursive(base, degree, [result]): float in negative degree
base as float, degree as int, result for inner usage
"""


def negative_degree_recursive(base, degree, result=0):
    if result == 0:
        result = base
    if degree > 1:
        result *= base
        return negative_degree_recursive(base, degree - 1, result)
    else:
        return 1/result


if __name__ == 'main':
    str_conv_num('')
    negative_degree_easy_mode(0, 0)
    negative_degree_cycle_mode(0, 0)
    negative_degree_recursive(0, 0)

