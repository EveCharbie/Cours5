import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return np.exp(x) / np.sqrt(np.sin(x)**3 + np.cos(x)**3)

def function_derivative(x):
    return (np.exp(x) * (2*np.sin(x)**3 + 2*np.cos(x)**3 + 3*np.sin(x)*np.cos(x)**2 - 3*np.sin(x)**2*np.cos(x))) \
           / (2*(np.sin(x)**3 + np.cos(x)**3)**(3/2))

def plot_finite_difference(vector_x, vector_y, exp):
    plt.figure()
    plt.plot(vector_x, function(vector_x), '.g', label="Points")
    plt.plot(np.arange(0, 100*10**-exp, 100**-exp), function(np.arange(0, 100*10**-exp, 100**-exp)), 'k', label="Vraie fonction")
    plt.plot(vector_x[1:-1], vector_y, '.b', label="Approximation")
    plt.plot(np.arange(0, 100*10**-exp, 100**-exp), function_derivative(np.arange(0, 100*10**-exp, 100**-exp)), 'r', label="Vraie dérivée")
    plt.legend()
    plt.show()
    return

fig, ax = plt.subplots(1, 1)
for exp in range(27):
    vector_x = np.arange(0, 100*10**-exp, 10**-exp)
    vector_y = (function(vector_x[2:]) - function(vector_x[:-2])) / (vector_x[2:] - vector_x[:-2])
    true_derivative = function_derivative(vector_x)
    # RMS normalized error
    error = np.mean(np.abs(vector_y - true_derivative[1:-1]) / np.abs(true_derivative[1:-1]))
    ax.plot(10**-exp, error, '.b')
    # plot_finite_difference(vector_x, vector_y, exp)
ax.invert_xaxis()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Taille du pas")
ax.set_ylabel("Erreur moyenne")
ax.set_title("Erreur de la différence finie centrée")
plt.savefig("diff_finine_erreur.png")
plt.show()