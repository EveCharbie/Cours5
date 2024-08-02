import numpy as np
import matplotlib.pyplot as plt


# Figure ppt
gauss_noised = np.random.normal(0, 10, 1000)
sinusoidal = 50*np.sin(np.linspace(0, 20*np.pi, 1000))
linear = 500*np.linspace(0, 1, 1000)
signal = linear + sinusoidal + gauss_noised

plt.figure()
plt.plot(signal, '.b', label="Signal", color="#5B80AB")
plt.legend()
plt.savefig("signal.png")
plt.show()


# Précision numpy
a = np.array([1.1, 2.2, 3.3])
print(f"Les éléments d'un array njumpy sont de type : {type(a[0])}")
print(f"Ils ont donc une précision de {np.finfo(a[0]).eps}")

def function(x_vector):
    return np.sin(x_vector)


# Intégration Simpson
dt = 0.01
x_vector = np.arange(0, 2*np.pi, dt)
h = (2*np.pi-0) / ((len(x_vector) - 1) / 2)
simpson = h/6 * (function(x_vector[0]) + 2*np.sum(function(x_vector[0:-2:2])) + 4*np.sum(function(x_vector[1:-2:2])) + function(x_vector[-1]))
trapeze = np.sum((function(x_vector[1:]) + function(x_vector[:-1])) / (2 * dt))


