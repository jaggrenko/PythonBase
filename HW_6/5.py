class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title}: запуск отрисовки...'


class Pen(Stationary):
    def draw(self):
        return f'__переопределение метода {self.draw}; {self.title}: запуск отрисовки...'


class Pensil(Stationary):
    def draw(self):
        return f'__переопределение метода {self.draw}* {self.title}: запуск отрисовки...'


class Handle(Stationary):
    def draw(self):
        return f'__переопределение метода {self.draw}! {self.title}: запуск отрисовки...'


pen = Pen('ручка')
print(pen.draw())

pensil = Pensil('карандаш')
print(pensil.draw())

handle = Handle('маркер')
print(handle.draw())
