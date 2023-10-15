import matplotlib.pyplot as plt

#нужно ввести 4 параметра для функций, по 2 нa каждую, коэфиициенты К и b
def linfunc(k1, b1, k2, b2):
    x = [i / 10 for i in range(0, 50, 1)]
    y1 = [(k1*i+b1) for i in x]
    y2 = [(k2*i+b2) for i in x]
    plt.title("Зависимости: y1 и y2")
    plt.xlabel("x")
    plt.ylabel("y1, y2")
    plt.grid()
    plt.plot(x, y1, x, y2)
    plt.show()