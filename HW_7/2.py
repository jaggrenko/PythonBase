from abc import ABC, abstractmethod


class Clothes(ABC):
    def __new__(cls, arg):
        if (isinstance(arg, int) or isinstance(arg, float)) and arg > 0:
            return super().__new__(cls)
        else:
            return None

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def calc(self) -> float:
        pass


class Suit(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def name(self):
        return f'костюм'

    def calc(self):
        return 2 * self.size + 0.3


class Coat(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def name(self):
        return f'пальто'

    def calc(self):
        return self.height / 6.5 + 0.5


try:
    suit = Suit(0)
    coat = Coat(1)
    print(f'Расход материала на {suit.name} и {coat.name}: {"{:.2f}".format(suit.calc() + coat.calc())}')
except TypeError:
    print(f'Ошибка: введите 1 аргумент - число > 0')
except AttributeError:
    print(f'Ошибка: введите число > 0')
