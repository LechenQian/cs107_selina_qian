import numpy as np
import matplotlib.pyplot as plt
import datetime

def len2coor(length):
    def coor(theta):
        x = length * np.cos(theta)
        y = length * np.sin(theta)
        return x,y
    return coor

count = 0
### Closure defined up here
# Specify the length of hour, minute and second hands
hour_len = 1
minute_len = 2
second_len = 2.5
fig = plt.figure(figsize=(6,6))
fig.canvas.draw()
while count < 100:
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second

    # Calculate theta in degrees for each hand

    theta_minute = (90 - 6*minute) * np.pi /180
    theta_second = (90 - 6*second) * np.pi /180
    theta_hour = (90 - 30*hour - 0.5*minute) * np.pi /180

    # hour_hand = name_of_closure(length_of_hour_hand)
    hour_hand = len2coor(hour_len)
    minute_hand = len2coor(minute_len)
    second_hand = len2coor(second_len)

    x_hour, y_hour = hour_hand(theta_hour)
    x_minute, y_minute = minute_hand(theta_minute)
    x_second, y_second = second_hand(theta_second)
    # Plot the clock

    # print(x_hour, y_hour)
    # print(x_minute, y_minute)
    # print(x_second, y_second)

    plt.plot([0,x_hour], [0,y_hour])
    plt.plot([0,x_minute],[0,y_minute])
    plt.plot([0,x_second], [0,y_second])
    plt.axis([-3, 3, -3, 3])
    plt.pause(0.1)
    plt.cla()
    count += 1
