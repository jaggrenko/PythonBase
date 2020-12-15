class Car:
    def __init__(self, speed, color, name, direction='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def car_direction(self):
        if self.direction == 'прямо':
            return f'{self.name} поехала {self.direction}'
        else:
            return f'{self.name} повернула {self.direction}'

    def show_speed(self):
        return f'текущая скорость: {self.speed}'

    def is_police_car(self):
        if self.is_police:
            return f'тип автомобиля: полицейский'
        else:
            return f'тип автомобиля: гражданский'


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
print(f'марка: {car_0.name}\nцвет: {car_0.color}\n'
      f'направление: {car_0.car_direction()}\n{car_0.is_police_car()}\n{car_0.show_speed()}\n')

car_1 = TownCar(40, 35, 'grey', 'volvo', 'направо')
print(f'марка: {car_1.name}\nцвет: {car_1.color}\n'
      f'направление: {car_1.car_direction()}\n{car_1.is_police_car()}\n{car_1.show_speed()}\n')

car_2 = SportCar(120, 100, 'red', 'maseratti', 'прямо')
print(f'марка: {car_2.name}\nцвет: {car_2.color}\n'
      f'направление: {car_2.car_direction()}\n{car_2.is_police_car()}\n{car_2.show_speed()}\n')

car_3 = PoliceCar(150, 'grey', 'UAZ', 'прямо', True)
print(f'марка: {car_3.name}\nцвет: {car_3.color}\n'
      f'направление: {car_3.car_direction()}\n{car_3.is_police_car()}\n{car_3.show_speed()}\n')
