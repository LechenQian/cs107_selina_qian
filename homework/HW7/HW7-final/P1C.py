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
    weather_class = Markov(weather)
    # load mc data
    weather_class.load_data('./weather.csv')
    # count the number of each weather type
    nums = Counter(weather_class.get_weather_for_day(7, 100))

    # save city, weather and number of weather in the dict structure
    w_prediction[city] = max(nums, key=nums.get)
    print("{}: {}".format(city, dict(nums)))

print("\n Most likely weather in seven days\n")

for city, weather in w_prediction.items():
    print("{}: {}".format(city, weather))
