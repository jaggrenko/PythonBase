class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Full name is: {self.name} {self.surname}'

    def get_total_income(self):
        return f'The total income of {self.name} {self.surname}: ' \
               f'{self._income["wage"] + self._income["bonus"]}'


ivanov = Position('Ivan', 'Ivanov', 'engineer', 100, 50)
print(ivanov.get_full_name())
print(ivanov.get_total_income())
