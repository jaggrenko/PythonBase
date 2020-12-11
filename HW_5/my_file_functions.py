from os import path


"""
f_lines_words (f_path as string, [word_delimiter=' '])
returns (int - lines count, int - words count) else -1, -1
"""


def f_lines_words(f_path, word_delimiter=' '):
    if path.isfile(f_path):
        words_count = 0
        with open(f_path) as f_obj:
            for lines_count, line in enumerate(f_obj, 1):
                words_count += line.count(word_delimiter)
            return lines_count, words_count + lines_count
    else:
        return -1, -1


"""
iterable_to_f (f_name as string, [f_mode as string] - default 'w', [f_encode as string] - default 'utf-8',
func as function, iter_obj as iterable (if not reverse), reverse as boolean - 
False: iterable to file {func args: file_object, el of iterable}, 
True: file to iterable {func args: file_object, el of file_object}
returns: boolean True if no errors else error as string
"""


def iterable_to_f(f_name, f_mode='w', f_encode='utf-8', func=None, iter_obj=None, reverse=False):
    if path.isfile(f_name):
        try:
            with open(f_name, f_mode, encoding=f_encode) as f_obj:
                if not reverse:
                    for el in iter_obj:
                        func(f_obj, el)
                else:
                    for el in f_obj:
                        func(f_obj, el)
            result = True
        except OSError as err:
            return err
        except TypeError as err:
            return err
        return result
    else:
        return f'{f_name} is not file'


if __name__ == 'main':
    f_lines_words('')
    iterable_to_f('')
