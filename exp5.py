import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Generate some sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 8, 18, 32, 50])

# Plot the original data
plt.scatter(x, y, label='Original Data', color='red')

# Perform linear interpolation
linear_interp = interp1d(x, y, kind='linear')
x_interp_linear = np.linspace(min(x), max(x), 100)
y_interp_linear = linear_interp(x_interp_linear)
plt.plot(x_interp_linear, y_interp_linear, label='Linear Interpolation', linestyle='--')

# Perform cubic spline interpolation
cubic_interp = interp1d(x, y, kind='cubic')
y_interp_cubic = cubic_interp(x_interp_linear)
plt.plot(x_interp_linear, y_interp_cubic, label='Cubic Spline Interpolation', linestyle='-.')

# Add titles and labels
plt.title('Interpolation Exercise')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()
