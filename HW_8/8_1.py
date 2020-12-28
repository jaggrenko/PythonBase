from datetime import datetime as dt


class Date:
    def __new__(cls, arg):
        try:
            dt.strptime(arg, '%m-%d-%Y')
        except ValueError:
            print('Ошибка: введите дату в формате "ДД-ММ-ГГГГ"')
            return None
        else:
            instance = object.__new__(cls)
            instance.inp_date = arg
            return instance

    @classmethod
    def date_extractor(cls, inp_date):
        try:
            __source = inp_date.split('-')
        except Exception:
            return None
        else:
            return __source

    @staticmethod
    # DD-MM-YYYY
    def date_validator():
        print(Date.date_extractor())


z = Date('03-03-2020')
z.date_validator()
