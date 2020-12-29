from abc import ABC, abstractmethod

# TODO: pickle as simuDB
item_type_lst = ('printer', 'scanner', 'xerox')


class Storage:
    def add_item(self):
        pass

    def rm_item(self):
        pass

    def cnt_item(self):
        pass

    def sort_item(self):
        pass


class OfficeEquip:
    # def __new__(cls, item_type: str, item_name: str, item_quantity: str, item_is_new: bool):
    #     try:
    #         if not ((item_type.isalpha() and item_type in item_type_lst)
    #                 and item_name.isalnum()
    #                 and item_quantity.isdigit()
    #                 and type(item_is_new) is bool):
    #             raise TypeError
    #             # instance = object.__new__(cls)
    #             # instance.item_type = item_type
    #             # instance.item_name = item_name
    #             # instance.item_quantity = item_quantity
    #             # instance.item_is_new = item_is_new
    #             # return instance
    #     except TypeError:
    #         print(f'Ошибка: введен неверный тип данных!')
    #         return None
    #     else:
    #         return object.__new__(cls)

    def __init__(self, item_type: str, item_name: str, item_quantity: str, item_is_new: bool):
        self.item_type = item_type
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_is_new = item_is_new


class Printer(OfficeEquip):
    def __init__(self, item_name: str, item_quantity: str, item_is_new: bool, is_color: bool, item_type: str = 'printer'):
        super().__init__(item_type, item_name, item_quantity, item_is_new)
        self.is_color = is_color


z = OfficeEquip('printer', '1d', '1', False)  # identationerror
print(z)

y = Printer('Lexmark', '1', True, False)
print(y.item_type, y.item_name, y.item_is_new, y.is_color, y.item_quantity)
