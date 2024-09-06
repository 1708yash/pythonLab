from scipy.optimize import minimize

# Objective function to minimize: f(x) = x1^2 + x2^2


def objective_function(x):
    return x[0]**2 + x[1]**2

# Equality constraint function: g(x) = x1 + x2 - 1


def constraint_equation(x):
    return x[0] + x[1] - 1

# Lagrangian function: Incorporates the objective function and the constraint


def lagrangian(x, lambda_):
    return objective_function(x) + lambda_ * constraint_equation(x)

# Wrapper function for scipy.optimize.minimize


def optimize_with_lagrange(initial_guess):
    # Define the constraint as a dictionary for scipy's minimize function
    constraints = {'type': 'eq', 'fun': constraint_equation}

    # Minimize the objective function under the given constraint
    result = minimize(objective_function, initial_guess,
                      constraints=constraints)
    return result


# Initial guess for optimization
initial_guess = [0.5, 0.5]

# Optimize using Lagrange multipliers
result = optimize_with_lagrange(initial_guess)

# Display the results
print("Optimal solution:", result.x)
print("Optimal value (Objective function value):", result.fun)

# Lagrange multiplier estimation (dual values are accessible through the solver)
lagrange_multiplier = result.jac @ result.x
print("Estimated Lagrange multiplier:", lagrange_multiplier)
