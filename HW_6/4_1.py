class Car:
    def __init__(self, speed_limit, speed, color, name, direction=''):
        self._speed_lim = speed_limit
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'...но внезапно {self.name} сделал(а) стоп'

    def car_direction(self):
        if self.direction == 'прямо':
            return f'{self.name} поехал(а) {self.direction}'
        else:
            return f'{self.name} повернул(а) {self.direction}'

    def show_speed(self):
        if self.speed > self._speed_lim:
            return f'превышение скорости {self.name}на {self.speed - self._speed_lim} км/ч!'
        else:
            return f'текущая скорость {self.name}: {self.speed} км/ч'

    def car_type(self):
        return f'{self.name} - это гражданский автомобиль'

    def __str__(self):
        return f'марка: {self.name}\nцвет: {self.color}\nтип автомобиля: {self.car_type()}\n' \
               f'направление: {self.car_direction()}\n{self.show_speed()}\n{self.stop()}\n'


class PoliceCar(Car):
    def car_type(self):
        return f'{self.name} - это полицейский автомобиль'

    def show_speed(self):
        return f'текущая скорость {self.name}: {self.speed} км/ч'


class TownCar(Car):
    pass


class WorkCar(Car):
    pass


class SportCar(Car):
    pass


car_0 = TownCar(60, 70, 'black', 'trabant', 'налево')
print(car_0)

car_1 = TownCar(40, 35, 'green', 'volvo', 'направо')
print(car_1)

car_2 = SportCar(120, 110, 'red', 'maseratti', 'прямо')
print(car_2)

car_3 = PoliceCar(0, 120, 'grey', 'Bobik', 'прямо')
print(car_3)
