from my_file_functions import f_lines_words


lines_cnt, words_cnt = f_lines_words('test.txt')
print(lines_cnt, words_cnt) if lines_cnt != -1 else print('Error')
