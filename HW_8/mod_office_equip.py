from mod_storage import Storage


class OfficeEquip:
    def __init__(self, item_type: str, item_name: str, item_is_new: bool, item_quantity: int,
                 item_in_stor: bool = True):
        self.item_type = item_type
        self.item_name = item_name.lower()
        self.item_is_new = item_is_new
        self.item_quantity = item_quantity
        self.item_in_stor = item_in_stor
        self.res_dict = {}

    def __call__(self, other=True):
        self.res_dict[self.item_type] = (self.item_name, self.item_is_new, other, self.item_quantity, self.item_in_stor)
        return self.res_dict


class Printer(OfficeEquip):
    def __init__(self, item_name, item_is_new, is_cmyk: bool, item_quantity):
        OfficeEquip.__init__(self, 'printer', item_name, item_is_new, item_quantity)
        self.is_cmyk = is_cmyk


class Scanner(OfficeEquip):
    def __init__(self, item_name, item_is_new, has_auto_feeder: bool, item_quantity):
        OfficeEquip.__init__(self, 'scanner', item_name, item_is_new, item_quantity)
        self.has_auto_feeder = has_auto_feeder


class Copier(OfficeEquip):
    def __init__(self, item_name, item_is_new, is_riso: bool, item_quantity):
        OfficeEquip.__init__(self, 'copier', item_name, item_is_new, item_quantity)
        self.is_riso = is_riso


if __name__ == '__main__':
    OfficeEquip('', '', False, 0)
    Printer('', False, False, 0)
    Scanner('', False, False, 0)
    Copier('', False, False, 0)
