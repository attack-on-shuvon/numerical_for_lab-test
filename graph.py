import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3-4*x-9

x= np.linspace(-5,5,50)

y = f(x)

plt.plot(x,y,label = "line")
plt.title("random f(x) graph")
plt.legend()
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("y axis")
plt.show()


