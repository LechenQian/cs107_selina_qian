from Markov import Markov

weather_today = Markov()
weather_today.load_data('./weather.csv')

# print(weather_today.get_prob('sunny', 'cloudy'))

# the probability that a windy day follows a cloudy day.
prob = weather_today.get_prob('cloudy', 'windy')
print('The probability that a windy day follows a cloudy day is {}'. format(prob))
