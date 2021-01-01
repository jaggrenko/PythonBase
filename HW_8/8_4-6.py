from my_stor import Storage


class OfficeEquip:
    def __init__(self, item_type: str, item_name: str, item_is_new: bool, item_quantity: int,
                 item_in_stor: bool = True):
        self.item_type = item_type
        self.item_name = item_name.lower()
        self.item_is_new = item_is_new
        self.item_quantity = item_quantity
        self.item_in_stor = item_in_stor
        self.res_dict = {}

    def __call__(self, other):
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


printer = Printer('Lexmark', True, False, 1)
printer.is_cmyk = True

s = Storage

s.add_item(printer(True))
s.mv_item('printer', 'lexmark', True, True, True, 2)
s.cnt_item('printer', 'lexmark', True)
s.cnt_item('printer', 'lexmark', False)

#s.rm_item('printer', 'lexmark', True, True, True, 2)
