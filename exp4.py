
def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        if abs(x2 - x1) < tol:
            print(f"Converged after {i+1} iterations.")
            return x2
        x0, x1 = x1, x2
    raise ValueError("Secant method did not converge")

def f(x):
    return x**2 - 4  


# Initial guesses
x0 = 1.0
x1 = 3.0

# Solve the equation using the Secant method
root = secant_method(f, x0, x1)
print(f"The root is: {root}")
