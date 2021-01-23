class Date:
    @classmethod
    def date_extractor(cls, dt_str):
        try:
            __source = dt_str.split('-')
        except AttributeError:
            print(f'Ошибка: дата должна быть задана в формате "ДД-ММ-ГГГГ"')
            return None
        except Exception as err:
            print(f'Ошибка: {err}')
        else:
            return __source

    @staticmethod
    def date_validator(dt_lst):
        try:
            dt_list = list(map(int, dt_lst))
            if dt_list[0] in range(1, 32) and dt_list[1] in range(1, 13):
                print(f'Дата введена корректно')
                return True
            else:
                raise ValueError(f'Ошибка: введите 0 < число < 32; 0 < месяц < 13')
        except ValueError as err:
            print(err)
            return False
        except TypeError:
            print(f'Ошибка: дата должна быть задана в формате "ДД-ММ-ГГГГ"')
            return False
        except Exception as err:
            print(f'Ошибка: {err}')
            return False        


z = Date.date_extractor('01-03-2020')
y = Date.date_validator(z)
