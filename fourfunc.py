import matplotlib.pyplot as plt
import math

def fourfunc():
    x = [i/10 for i in range(0, 50, 1)]
    y1 = [math.cos(i) for i in x]
    y2 = [math.sin(i) for i in x]
    y3 = [i**2 for i in x]
    y4 = []
    for i in x:
        if i == 0:
            y4.append(None)
        else:
            y4.append(2/i)
    # Построение графиков
    plt.figure("4 функции", figsize=(12, 12))
    plt.subplot(2, 2, 1) # Вложенный график 1
    plt.plot(x, y1)
    plt.title("y = cos(x)")
    plt.ylabel("y1")
    plt.grid(True)

    plt.subplot(2, 2, 2) # Вложенный график 2
    plt.plot(x, y2)
    plt.title("y = sin(x)")
    plt.ylabel("y2")
    plt.grid(True)

    plt.subplot(2, 2, 3)  # Вложенный график 3
    plt.plot(x, y3)
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y3")
    plt.grid(True)

    plt.subplot(2, 2, 4)  # Вложенный график 4
    plt.plot(x, y4)
    plt.title("y = x/2")
    plt.xlabel("x")
    plt.ylabel("y4")
    plt.grid(True)
    plt.show()

fourfunc()