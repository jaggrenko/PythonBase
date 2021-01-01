import argparse as ap


def loan_calc(hours, hour_rate, bonus):
    return hours * hour_rate + bonus


parser = ap.ArgumentParser(description='Calculate loan of employee')
parser.add_argument('-r', action='store', dest='hour_rate', type=float, required=True, help='Почасовая ставка')
parser.add_argument('-t', action='store', dest='hours', type=int, required=True, help='Количество часов')
parser.add_argument('-b', action='store', dest='bonus', type=float, required=True, help='Размер премии')

args = parser.parse_args()

print(loan_calc(args.hours, args.hour_rate, args.bonus))
