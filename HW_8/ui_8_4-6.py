import argparse
from mod_office_equip import Printer, Scanner, Copier
from mod_storage import Storage

# office_equipment = oe
cmd: str = ''
type_oe: str = ''
brand_oe: str = ''
quant_oe: int = 0
is_new_oe: bool = False
special_func: bool = False
to_storage: bool = True

parser = argparse.ArgumentParser(description=f'Manage storage. Main commands: add(type, brand, attr, quantity) * '
                                             'rm(type, brand, new, attr, stor/office, quantity) * '
                                             'mv(type, brand, new, attr, stor/office, quantity) * '
                                             'cnt(type, brand, stor/office)')

parser.add_argument('-c', action='store', dest='cmd', type=str, required=True, help='Команда: add, rm, mv, cnt')
parser.add_argument('-type', action='store', dest='type_oe', type=str, required=True, help='Вид офисной техники: '
                                                                                           'printer, scanner, copier')
parser.add_argument('-brand', action='store', dest='brand_oe', type=str, required=True, help='Марка (бренд) офисной '
                                                                                             'техники')
parser.add_argument('-quant', action='store', dest='quant_oe', type=int, required=True, help='Количество')
parser.add_argument('-new', action='store', dest='is_new_oe', type=bool, required=True, help='Состояние: новая - б/у')
parser.add_argument('-spec', action='store', dest='special_func', type=bool, required=False, help='Отличительная черта '
                                                                                                 'в классе (принтер '
                                                                                                 'цветной: да/нет)')
parser.add_argument('-stor', action='store', dest='to_storage', type=bool, required=False, help='На склад: да/нет')

args = parser.parse_args()

s = Storage

print(cmd)
if cmd == 'add':
    print('in')
    if type_oe == 'printer':
        obj = Printer(brand_oe, is_new_oe, special_func, quant_oe)
        s.add_item(obj())
    elif type_oe == 'scanner':
        obj = Scanner(brand_oe, is_new_oe, special_func, quant_oe)
        s.add_item(obj())
    elif type_oe == 'copier':
        obj = Copier(brand_oe, is_new_oe, special_func, quant_oe)
        s.add_item(obj())
    else:
        print(f'Неизвестный тип офисной техники')
