from time import sleep


class TrafficLight:
    def __init__(self, cycles_count):
        self._cycles_cnt = cycles_count
        self.__color_timing = ({'red': 4}, {'yellow': 2}, {'green': 4})
        self.__trl_sequence = {'red': 'yellow', 'yellow': 'green', 'green': 'yellow'}
        self.__reversed = False

    def __process_msg(self, key=None, val=None):
        __next_color = 'red' if self.__reversed and key == 'yellow' else self.__trl_sequence[key]
        print(f'Сейчас горит {key}.\n'
              f'До смены сигнала --> {__next_color} {val} сек.')

    def __ticks(self):
        sleep(1)

    def __flag_switch(self):
        self.__reversed = not self.__reversed

    def __driver(self, iter_2_layers):
        for item in iter_2_layers:
            for key, val in item.items():
                while val > 1:
                    val -= 1
                    self.__process_msg(key, val)
                    self.__ticks()

    def running(self):
        for _ in range(self._cycles_cnt):
            self.__driver(self.__color_timing[1::-1]) if self.__reversed else self.__driver(self.__color_timing)
            self.__flag_switch()


trl = TrafficLight(2)
trl.running()
