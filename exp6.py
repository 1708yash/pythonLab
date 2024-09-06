import numpy as np
import matplotlib.pyplot as plt

# Function to integrate


def func(x):
    return x ** 2

# Trapezoidal rule implementation


def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return integral

# Simpson's rule implementation


def simpsons_rule(func, a, b, n):
    if n % 2 == 1:  # Simpson's rule requires an even number of intervals
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) +
                        2 * np.sum(y[2:-2:2]) + y[-1])
    return integral


# Define integration bounds
a, b = 0, 2

# True integral value for comparison (integral of x^2 from 0 to 2)
true_value = (b**3 - a**3) / 3

print(f'True Integral Value: {true_value:.4f}')

# Experiment with different values of n
n_values = [4, 8, 16, 32, 64]

# Perform integration and print results
for n in n_values:
    trapezoidal_result = trapezoidal_rule(func, a, b, n)
    simpsons_result = simpsons_rule(func, a, b, n)
    print(f'n={n}: Trapezoidal Result={
          trapezoidal_result:.4f}, Simpson\'s Result={simpsons_result:.4f}')

# Plot the function and the area under the curve
x_values = np.linspace(a, b, 100)
plt.plot(x_values, func(x_values), label='$x^2$ function')
plt.fill_between(x_values, func(x_values), alpha=0.2,
                 label='Area under the curve')

# Show the plot and legend
plt.title('Numerical Integration Experiment')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
