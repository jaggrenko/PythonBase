import argparse
from mod_office_equip import Printer, Scanner, Copier
from mod_storage import Storage


def yn_as_bool(arg: str):
    return True if arg.lower() == 'y' else False


# office_equipment = oe
parser = argparse.ArgumentParser(description=f'Manage storage. Main commands: add(type, brand, attr, quantity) * '
                                             'rm(type, brand, new, attr, stor/office, quantity) * '
                                             'mv(type, brand, new, attr, stor/office, quantity) * '
                                             'cnt(type, brand, stor/office)')

parser.add_argument('-c', action='store', dest='cmd', type=str, required=True, help='Команда: add, rm, mv, cnt')
parser.add_argument('-type', action='store', dest='type_oe', type=str, required=True, help='Вид офисной техники: '
                                                                                           'printer, scanner, copier')
parser.add_argument('-brand', action='store', dest='brand_oe', type=str, required=True, help='Марка (бренд) офисной '
                                                                                             'техники')
parser.add_argument('-quant', action='store', dest='quant_oe', type=int, required=False, help='Количество')
parser.add_argument('-new', action='store', dest='is_new_oe', type=str, required=False, help='Состояние: новая - y/n')
parser.add_argument('-spec', action='store', dest='special_func', type=str, required=False, help='Отличительная черта '
                                                                                                  'в классе (принтер '
                                                                                                  'цветной: y/n)')
parser.add_argument('-stor', action='store', dest='to_storage', type=str, required=False, help='На склад: y/n')

args = parser.parse_args()

s = Storage
yn = yn_as_bool

if args.cmd == 'add':
    if args.type_oe == 'printer':
        cl = Printer
    elif args.type_oe == 'scanner':
        cl = Scanner
    elif args.type_oe == 'copier':
        cl = Copier
    else:
        cl = None

    if cl:
        obj = cl(args.brand_oe, yn(args.is_new_oe), yn(args.special_func), args.quant_oe)
        s.add_item(obj())
    else:
        print(f'Неизвестный тип офисной техники')

elif args.cmd == 'cnt':
    s.cnt_item(args.type_oe, args.brand_oe, yn(args.to_storage))
elif args.cmd == 'mv':
    s.mv_item(args.type_oe, args.brand_oe, yn(args.is_new_oe), yn(args.special_func), yn(args.to_storage), args.quant_oe)
elif args.cmd == 'rm':
    s.rm_item(args.type_oe, args.brand_oe, yn(args.is_new_oe), yn(args.special_func), yn(args.to_storage), args.quant_oe)
