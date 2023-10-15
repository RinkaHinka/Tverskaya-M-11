import matplotlib.pyplot as plt
from random import randint

def stolb():
    fruits = ["яблоки", "груши",
              "апельсины", "бананы",
              "лимоны", "абрикосы", "персики"]
    counts = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
    plt.bar(fruits, counts)
    plt.title("Фрукты")
    plt.xlabel("фрукты")
    plt.ylabel("кол-во покупок в день (шт)")
    plt.grid()
    plt.show()
stolb()