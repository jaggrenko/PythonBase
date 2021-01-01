my_list = [None, True, b'bytes', 1, 8.5, complex(6, 5), 'g', 'abc', lambda x: x+2]

# [print(f'El {index}: {type(my_list[index])}') for index in range(len(my_list))]
[print(f'El {index}: {type(El)}') for index, El in enumerate(my_list)]
