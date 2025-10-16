import numpy as np
import matplotlib.pyplot as plt

# Ask user for number of measurements
n = int(input("Enter number of measurements: "))

# Get x values
x = []
print("Enter x values:")
for i in range(n):
    val = float(input(f"x[{i+1}]: "))
    x.append(val)

# Get y values
y = []
print("Enter y values:")
for i in range(n):
    val = float(input(f"y[{i+1}]: "))
    y.append(val)

# Convert to numpy arrays
x = np.array(x)
y = np.array(y)

# Fit linear regression (y = mx + b)
m, b = np.polyfit(x, y, 1)

# Create regression line for plotting
y_fit = m * x + b

# Plot points
plt.scatter(x, y, color='red', label='Data points')

# Plot regression line
plt.plot(x, y_fit, color='blue', label=f'Fit: y = {m:.2f}x + {b:.2f}')

# Labels and legend
plt.xlabel("Freq(e14Hz)")
plt.ylabel("Uo(V)")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)

# Show plot
plt.show()

# Print the result
print(f"\nEquation of best fit: y = {m:.4f}x + {b:.4f}")

