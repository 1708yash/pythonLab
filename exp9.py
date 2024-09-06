from scipy.optimize import minimize

# Objective function to minimize: f(x) = x1^2 + x2^2


def objective_function(x):
    return x[0]**2 + x[1]**2

# Equality constraint function: g1(x) = x1 + x2 - 1 = 0


def equality_constraint(x):
    return x[0] + x[1] - 1

# Inequality constraint function: g2(x) = x1 - x2 >= 0


def inequality_constraint(x):
    return x[0] - x[1]


# Initial guess for optimization
initial_guess = [0.5, 0.5]

# Define constraints: One equality and one inequality
constraints = [
    {'type': 'eq', 'fun': equality_constraint},  # x1 + x2 = 1
    {'type': 'ineq', 'fun': inequality_constraint}  # x1 >= x2
]

# Optimize with equality and inequality constraints
result = minimize(objective_function, initial_guess, constraints=constraints)

# Display the results
print("Optimal solution:", result.x)
print("Optimal value (Objective function value):", result.fun)
