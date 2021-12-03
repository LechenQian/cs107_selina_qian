import numpy as np


class Markov:
    def __init__(self, day_zero_weather=None):
        self.data = np.array([])
        self.d = {'sunny': 0, 'cloudy': 1, 'rainy': 2, 'snowy': 3, 'windy': 4, 'hailing': 5}
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        self._current_day_weather = day_zero_weather

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather):
        if current_day_weather not in self.d:
            raise Exception("Current day has not been specified!")

        if next_day_weather not in self.d:
            raise Exception("Next day has not been specified!")

        return self.data[self.d[current_day_weather], self.d[next_day_weather]]

    def __iter__(self):
        return MarkovIterator(self, self.day_zero_weather)

    def _reset(self):
        self._current_day_weather = self.day_zero_weather
        self._current_day = 0

    def _simulate_weather_for_day(self, day):
        if day < 0:
            raise Exception("Day is less than 0")
        self._reset()

        if day == 0:
            return self._current_day_weather

        for num_day in range(day):
            next_weather = next(iter(self))
        return next_weather

    def get_weather_for_day(self, day, trials=100):
        if trials <= 0 or day < 0:
            raise Exception("Input should be non-negative")

        weathers = []
        for i in range(trials):
            weathers.append(self._simulate_weather_for_day(int(day)))
        return weathers


class MarkovIterator:
    def __init__(self, mk, day_zero_weather):
        self.mk = mk
        self.current = day_zero_weather

    def __iter__(self):
        return self

    def __next__(self):
        next_day_prob = [self.mk.get_prob(self.current, i) for i in self.mk.d.keys()]
        self.current = np.random.choice(a=list(self.mk.d.keys()), p=next_day_prob)
        return self.current
