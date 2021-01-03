import shelve as sh


class Storage:
    # cls variables used as list indexes except @classmethod 'add_item()'
    ind_new = 0
    ind_attr = 1
    ind_qnty = 2
    ind_stor = -1

    @classmethod
    def add_item(cls, equip_dict):
        # --> equip_dict.items structure: ('item_type': item_name, item_is_new, spec_attrib, item_quant, item_in_stor)
        key, val = None, None
        try:
            for key, val in equip_dict.items():
                with sh.open(f'{key}.md') as sh_obj:
                    if val[0] in sh_obj:
                        tmp_lst = sh_obj[val[0]][:]
                        # {'item_name': (item_is_new, spec_attrib, item_quant, item_in_stor)} -->
                        tmp_lst.append(val[1:])
                        sh_obj[val[0]] = tmp_lst
                    else:
                        sh_obj[val[0]] = [val[1:]]
            else:
                cls._optimizer(key, val[0])
                print(f'Добавлено: {val[3]} ед. техники [{key}:{val[0]}] --> склад')
        except LookupError as err:
            print(f'Ошибка (ключ [{val[0]}]): {err}')
        except OSError as err:
            print(f'Ошибка {err.errno}: {err.strerror}')

    @classmethod
    def rm_item(cls, item_type: str, item_name: str, item_is_new: bool, item_has_attr: bool, item_in_stor: bool,
                cnt_to_rm: int):
        try:
            with sh.open(f'{item_type}.md') as sh_obj:
                tmp_lst = sh_obj[item_name][:]
                for i, el in enumerate(tmp_lst):
                    match: bool = el[cls.ind_new] == item_is_new and el[cls.ind_attr] == item_has_attr \
                                  and el[cls.ind_stor] == item_in_stor
                    if match and el[cls.ind_qnty] > 0:
                        new_cnt = el[cls.ind_qnty] - cnt_to_rm
                        if new_cnt >= 0:
                            tmp_lst[i] = (el[cls.ind_new], el[cls.ind_attr], new_cnt, el[cls.ind_stor])
                            sh_obj[item_name] = tmp_lst
                            success_msg = f'Техника [{item_type}:{item_name}] с заданными параметрами в количестве ' \
                                          f'{cnt_to_rm} ед. удалена <-- '
                            print(f'{success_msg}склад') if item_in_stor else print(f'{success_msg}подразделения')
                            return True
                        else:
                            print(f'Введите значение не превышающее {el[cls.ind_qnty]}')
                            return False
                    elif match and el[cls.ind_qnty] <= 0:
                        print(f'Техника [{item_type}:{item_name}] с заданными параметрами отсутствует')
                        return False
        except LookupError as err:
            print(f'Ошибка [{item_type}:{item_name}]): {err}')
        except OSError as err:
            print(f'Ошибка {err.errno}: {err.strerror}')

    @classmethod
    def mv_item(cls, item_type: str, item_name: str, item_is_new: bool, item_has_attr: bool, item_in_stor: bool,
                cnt_to_mv: int):
        if cls.rm_item(item_type, item_name, item_is_new, item_has_attr, item_in_stor, cnt_to_mv):
            try:
                with sh.open(f'{item_type}.md') as sh_obj:
                    tmp_lst = sh_obj[item_name][:]
                    for i, el in enumerate(tmp_lst):
                        match = el[cls.ind_new] == item_is_new and el[cls.ind_attr] == item_has_attr \
                                and el[cls.ind_stor] == (not item_in_stor)
                        if match:
                            new_cnt = el[cls.ind_qnty] + cnt_to_mv
                            tmp_lst[i] = (el[cls.ind_new], el[cls.ind_attr], new_cnt, el[cls.ind_stor])
                            sh_obj[item_name] = tmp_lst
                            success_msg = f'Техника [{item_type}:{item_name}] с заданными параметрами в количестве ' \
                                          f'{cnt_to_mv} ед. перемещена: '
                            print(f'{success_msg}склад --> подразделения') if item_in_stor \
                                else print(f'{success_msg}подразделения --> склад')
            except LookupError as err:
                print(f'Ошибка [{item_type}:{item_name}]): {err}')
            except OSError as err:
                print(f'Ошибка {err.errno}: {err.strerror}')

    @classmethod
    def cnt_item(cls, item_type: str, item_name: str, item_in_stor: bool):
        try:
            with sh.open(f'{item_type}.md') as sh_obj:
                tmp_lst = sh_obj[item_name][:]
                tmp_val_in = 0
                tmp_val_out = 0
                for el in tmp_lst:
                    if el[cls.ind_stor]:
                        tmp_val_in += el[cls.ind_qnty]
                    else:
                        tmp_val_out += el[cls.ind_qnty]
                else:
                    print(f'Всего на складе [{item_type}:{item_name}]: {tmp_val_in} ед.') if item_in_stor \
                        else print(f'Передано подразделениям [{item_type}:{item_name}]: {tmp_val_out} ед.')
        except LookupError as err:
            print(f'Ошибка [{item_type}:{item_name}]): {err}')
        except OSError as err:
            print(f'Ошибка {err.errno}: {err.strerror}')

    @classmethod
    def _optimizer(cls, item_type: str, item_name: str):
        # new_has_in_stor, new_has_out_stor, old_has_in_stor, old_has_out_stor,
        # new_hasnt_in_stor, new_hasnt_out_stor, old_hasnt_in_stor, old_hasnt_out_stor
        states = [0, 0, 0, 0, 0, 0, 0, 0]
        mask = [(True, True, True), (True, True, False), (False, True, True), (False, True, False),
                (True, False, True), (True, False, False), (False, False, True), (False, False, False)]
        try:
            with sh.open(f'{item_type}.md') as sh_obj:
                tmp_lst = sh_obj[item_name][:]
                for el in tmp_lst:
                    tmp_tuple = tuple([el[cls.ind_new], el[cls.ind_attr], el[cls.ind_stor]])
                    try:
                        states[mask.index(tmp_tuple)] += el[cls.ind_qnty]
                    except ValueError:
                        continue
                else:
                    mask = list(map(list, mask))
                    [mask[i].insert(2, states[i]) for i, val in enumerate(mask)]
                    sh_obj[item_name] = list(map(tuple, mask))
        except LookupError as err:
            print(f'Ошибка [{item_type}:{item_name}]): {err}')
        except OSError as err:
            print(f'Ошибка {err.errno}: {err.strerror}')

    #TODO: cnt_item extended
    # @classmethod
    # def sort_item(self):
    #     pass


if __name__ == '__main__':
    Storage()
