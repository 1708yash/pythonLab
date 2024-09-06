import numpy as np
from pyswarm import pso

# Define the multidimensional objective function to minimize


def objective_function(x):
    return np.sum(x**2)


# Set the search space bounds (example: 3-dimensional space)
lower_bound = [-5, -5, -5]
upper_bound = [5, 5, 5]

# Perform PSO optimization
best_solution, best_value = pso(objective_function, lower_bound, upper_bound)

# Display the results
print("Optimal solution:", best_solution)
print("Optimal value:", best_value)
