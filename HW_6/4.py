class Car:
    def __init__(self, speed, color, name, direction='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехал(а)'

    def stop(self):
        return f'{self.name} ...сделал(а) стоп'

    def car_direction(self):
        if self.direction == 'прямо':
            return f'{self.name} поехал(а) {self.direction}'
        else:
            return f'{self.name} повернул(а) {self.direction}'

    def show_speed(self):
        return f'текущая скорость: {self.speed}'

    def is_police_car(self):
        if self.is_police:
            return f'полицейский'
        else:
            return f'гражданский'

    def __str__(self):
        return f'марка: {self.name}\nцвет: {self.color}\nтип автомобиля: {self.is_police_car()}\n' \
               f'направление: {self.car_direction()}\n{self.show_speed()}\n{self.stop()}\n'


class TownCar(Car):
    def __init__(self, speed_limit, speed, color, name, direction):
        super().__init__(speed, color, name, direction)
        self._speed_lim = speed_limit

    def show_speed(self):
        if self.speed > self._speed_lim:
            return f'превышение скорости {self.name} на {self.speed - self._speed_lim} км/ч!'
        else:
            return f'текущая скорость {self.name}: {self.speed}'


class WorkCar(Car):
    def __init__(self, speed_limit, speed, color, name, direction):
        super().__init__(speed, color, name, direction)
        self._speed_lim = speed_limit

    def show_speed(self):
        if self.speed > self._speed_lim:
            return f'Превышение скорости {self.name} на {self.speed - self._speed_lim} км/ч!'
        else:
            return f'Текущая скорость {self.name}: {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed_limit, speed, color, name, direction):
        super().__init__(speed, color, name, direction)
        self._speed_lim = speed_limit

    def show_speed(self):
        if self.speed > self._speed_lim:
            return f'Превышение скорости {self.name} на {self.speed - self._speed_lim} км/ч!'
        else:
            return f'Текущая скорость {self.name}: {self.speed} км/ч'


class PoliceCar(Car):
    pass


car_0 = TownCar(60, 70, 'black', 'trabant', 'налево')
print(car_0)

car_1 = TownCar(40, 35, 'grey', 'volvo', 'направо')
print(car_1)

car_2 = SportCar(120, 100, 'red', 'maseratti', 'прямо')
print(car_2)

car_3 = PoliceCar(150, 'grey', 'UAZ', 'прямо', True)
print(car_3)
