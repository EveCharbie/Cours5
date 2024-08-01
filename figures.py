import numpy as np
import matplotlib.pyplot as plt

gauss_noised = np.random.normal(0, 10, 1000)
sinusoidal = 50*np.sin(np.linspace(0, 20*np.pi, 1000))
linear = 500*np.linspace(0, 1, 1000)
signal = linear + sinusoidal + gauss_noised

plt.figure()
plt.plot(signal, '.b', label="Signal", color="#5B80AB")
plt.legend()
plt.savefig("signal.png")
plt.show()

a = np.array([1.1, 2.2, 3.3])
print(f"Les éléments d'un array njumpy sont de type : {type(a[0])}")
print(f"Ils ont donc une précision de {np.finfo(a[0]).eps}")


