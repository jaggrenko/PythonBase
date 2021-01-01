class Road:
    __WEIGHT_1SQRM = 25

    def __init__(self, road_width, road_length, road_height):
        self._road_width = road_width
        self._road_length = road_length
        self._road_height = road_height

    def mass_calc(self):
        print(f'{self._road_length / 1000 * self._road_width * self._road_height * self.__WEIGHT_1SQRM} т')


road_to_hell = Road(20, 5000, 5)
road_to_hell.mass_calc()
