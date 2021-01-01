import shelve as sh


class Storage:
    @classmethod
    def add_item(cls, equip_dict):
        for key, val in equip_dict.items():
            with sh.open(f'{key}.md') as sh_obj:
                if len(sh_obj) < 1:  # or not in obj keys()
                    sh_obj[val[0]] = [val[1:]]
                else:
                    tmp_lst = sh_obj[val[0]]
                    tmp_lst.append(val[1:])
                    sh_obj[val[0]] = tmp_lst

    @classmethod
    def rm_item(cls, item_type: str, item_name: str, item_in_stor: bool):
        with sh.open(f'{item_type}.md') as sh_obj:
            val = sh_obj[item_name][:]
            val = list(val)
            val[-1] = False
            sh_obj[val[0]] = [tuple(val[1:])]

    def mv_item(self):
        pass

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
                if item_in_stor:
                    print(f'На складе: {tmp_val_in}')
                else:
                    print(f'Передано: {tmp_val_out}')
    @classmethod
    def optimizer(cls, item_type: str, item_name: str):
        dict_opt = []
        new_has_in_stor = 0
        new_has_out_stor = 0
        old_has_in_stor = 0
        old_has_out_stor = 0
        new_hasnt_in_stor = 0
        new_hasnt_out_stor = 0
        old_hasnt_in_stor = 0
        old_hasnt_out_stor = 0
        with sh.open(f'{item_type}.md') as sh_obj:
            val = sh_obj[item_name][:]
            for el in val:
                if val[1] and val[2] and val[-1]:
                    new_has_in_stor += val[3]
                elif val[1] and val[2] and not val[-1]:
                    new_has_out_stor += val[3]
                elif not val[1] and val[2] and val[-1]:
                    old_has_in_stor += val[3]
                elif not val[1] and val[2] and not val[-1]:
                    old_has_out_stor += val[3]
                elif val[1] and not val[2] and val[-1]:
                    new_hasnt_in_stor += val[3]
                elif val[1] and not val[2] and not val[-1]:
                    new_hasnt_out_stor += val[3]
                elif not val[1] and not val[2] and val[-1]:
                    old_hasnt_in_stor += val[3]
                elif not val[1] and not val[2] and not val[-1]:
                    old_hasnt_out_stor += val[3]
            else:
                val_sorted = [(True, True, new_has_in_stor, True),
                              (True, True, new_has_out_stor, False),
                              (False, True, old_has_in_stor, True),
                              (False, True, old_has_out_stor, False),
                              ###
                              (True, False, new_hasnt_in_stor, True),
                              (True, False, new_hasnt_out_stor, False),
                              (False, False, old_hasnt_in_stor, True),
                              (False, False, old_hasnt_out_stor, False)]
                sh_obj[item_name] = val_sorted

    def sort_item(self):
        pass


if __name__ == '__main__':
    Storage()
