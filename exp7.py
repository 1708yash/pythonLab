import numpy as np
import matplotlib.pyplot as plt

# Function to differentiate


def func(x):
    return x ** 2

# True derivative for comparison (since we know the derivative of x^2 is 2x)


def true_derivative(x):
    return 2 * x

# Finite difference method for numerical differentiation (forward difference)


def forward_difference(func, x, h):
    return (func(x + h) - func(x)) / h


# Define parameters
x_value = 2.0
h_values = [0.1, 0.01, 0.001]

# Calculate true derivative
true_derivative_value = true_derivative(x_value)
print(f'True Derivative Value at x={x_value}: {true_derivative_value:.4f}')

# Experiment with different values of h
for h in h_values:
    numerical_derivative = forward_difference(func, x_value, h)
    print(f'h={h}: Numerical Derivative={numerical_derivative:.4f}')

# Plot the function and tangent line for visualization
x_values = np.linspace(0, 4, 100)
plt.plot(x_values, func(x_values), label='$x^2$ function')
plt.scatter(x_value, func(x_value), color='red', label='Point of Interest')

# Plot tangent lines for different h values
for h in h_values:
    tangent_line = true_derivative_value * (x_values - x_value) + func(x_value)
    plt.plot(x_values, tangent_line, label=f'Tangent (h={h})', linestyle='--')

# Show the plot and legend
plt.title('Numerical Differentiation Experiment')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
