import shelve as sh


class Storage:
    @classmethod
    def add_item(cls, equip_dict):
        for key, val in equip_dict.items():
            with sh.open(f'{key}.md') as sh_obj:
                if len(sh_obj) < 1:  # or not in obj keys()
                    sh_obj[val[0]] = [val[1:]]
                else:
                    tmp_lst = sh_obj[val[0]][:]
                    tmp_lst.append(val[1:])
                    sh_obj[val[0]] = tmp_lst
        else:
            cls._optimizer(key, val[0])

    @classmethod
    def rm_item(cls, item_type: str, item_name: str, item_is_new: bool, item_has_attr: bool, item_in_stor: bool,
                cnt_to_rm: int):
        with sh.open(f'{item_type}.md') as sh_obj:
            val = sh_obj[item_name][:]
            for i, el in enumerate(val):
                match = el[0] == item_is_new and el[1] == item_has_attr and el[-1] == item_in_stor
                if match and el[2] > 0:
                    new_cnt = el[2] - cnt_to_rm
                    if new_cnt >= 0:
                        val[i] = (el[0], el[1], new_cnt, el[-1])
                        sh_obj[item_name] = val
                        if item_in_stor:
                            print(f'Техника [{item_type}:{item_name}] с заданными параметрами в количестве {cnt_to_rm} '
                                  f'ед. удалена со склада')
                        else:
                            print(f'Техника [{item_type}:{item_name}] с заданными параметрами в количестве {cnt_to_rm} '
                                  f'ед. удалена из подразделения')
                        return True
                    else:
                        print(f'Введите значение не больше {el[2]}')
                        return False
                elif match and el[2] <= 0:
                    print(f'Техника [{item_type}:{item_name}] с заданными параметрами отсутствует')
                    return False

    @classmethod
    def mv_item(cls, item_type: str, item_name: str, item_is_new: bool, item_has_attr: bool, item_in_stor: bool,
                cnt_to_mv: int):
        if cls.rm_item(item_type, item_name, item_is_new, item_has_attr, item_in_stor, cnt_to_mv):
            with sh.open(f'{item_type}.md') as sh_obj:
                val: list = sh_obj[item_name][:]
                for i, el in enumerate(val):
                    match = el[0] == item_is_new and el[1] == item_has_attr and el[-1] == (not item_in_stor)
                    if match:
                        new_cnt = el[2] + cnt_to_mv
                        val[i] = (el[0], el[1], new_cnt, el[-1])
                        sh_obj[item_name] = val
                        if item_in_stor:
                            print(f'Техника [{item_type}:{item_name}] с заданными параметрами в количестве {cnt_to_mv} '
                                  f'ед. перемещена со склада в подразделения')
                        else:
                            print(f'Техника [{item_type}:{item_name}] с заданными параметрами в количестве {cnt_to_mv} '
                                  f'ед. перемещена из подразделения на склад')

    @classmethod
    def cnt_item(cls, item_type: str, item_name: str, item_in_stor: bool):
        with sh.open(f'{item_type}.md') as sh_obj:
            val = sh_obj[item_name][:]
            tmp_val_in = 0
            tmp_val_out = 0
            for el in val:
                if el[-1]:
                    tmp_val_in += el[2]
                else:
                    tmp_val_out += el[2]
            else:
                print(f'Всего на складе [{item_type}:{item_name}]: {tmp_val_in} ед.') if item_in_stor \
                    else print(f'Всего передано [{item_type}:{item_name}]: {tmp_val_out} ед.')

    @classmethod
    def _optimizer(cls, item_type: str, item_name: str):
        # new_has_in_stor, new_has_out_stor, old_has_in_stor, old_has_out_stor,
        # new_hasnt_in_stor, new_hasnt_out_stor, old_hasnt_in_stor, old_hasnt_out_stor
        states = [0, 0, 0, 0, 0, 0, 0, 0]
        mask = [(True, True, True), (True, True, False), (False, True, True), (False, True, False),
                (True, False, True), (True, False, False), (False, False, True), (False, False, False)]

        with sh.open(f'{item_type}.md') as sh_obj:
            val = sh_obj[item_name][:]
            for el in val:
                tmp_tuple = tuple([el[0], el[1], el[-1]])
                try:
                    states[mask.index(tmp_tuple)] += el[2]
                except ValueError:
                    continue
            else:
                mask = list(map(list, mask))
                [mask[i].insert(2, states[i]) for i, val in enumerate(mask)]
                sh_obj[item_name] = list(map(tuple, mask))

    def sort_item(self):
        pass


if __name__ == '__main__':
    Storage()
