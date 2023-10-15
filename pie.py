import matplotlib.pyplot as plt
from random import randint

def pie(n):
    labels = []
    values = []
    for i in range(1, n + 1):
        labels.append(i)
    a = 0
    for i in range(n):
        values.append(randint(1, 100))
        a += values[i]
    b = 0
    for i in range(n-1):
        b += values[i]
    if a < 100:
        values[-1] = 100 - b
    for i in range(n):
        a += values[i]
    plt.pie(values, labels=labels)
    plt.show()

pie(10)