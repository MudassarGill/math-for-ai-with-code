def c_to_f(c):
    return 1.8*c + 32

print(c_to_f(25))  # 77°F
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2  # simple quadratic function

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x) = x^2")
plt.title("Function Graph")
plt.grid(True)
plt.show()