from Markov import Markov
from collections import Counter

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}


w_prediction = {}
for city, weather in city_weather.items():
    weather_ = Markov(weather)
    weather_.load_data('./weather.csv')
    nums = Counter(weather_.get_weather_for_day(7, 100))
    w_prediction[city] = max(nums.items(), key=lambda x: x[1])[0]
    print("{}: {}".format(city, dict(nums)))


print("\n Most likely weather in seven days")
print("----------------------------------")
for city, weather in w_prediction.items():
    print("{}: {}".format(city, weather))

