import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generate sample data
x = np.linspace(0, 10, 20)
y = 3*x + 2 + np.random.normal(0, 1, len(x))

# Linear regression
res = linregress(x, y)

print("Slope =", res.slope)
print("Intercept =", res.intercept)
print("R-value =", res.rvalue)

# Plot
plt.scatter(x, y, label="Data")
plt.plot(x, res.slope*x + res.intercept, label="Fit", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Fit")
plt.grid()
plt.legend()
plt.show()
plt.savefig("../plots/linearfit.png")

# ----------------------------------------------------------
# THEORY (BRIEF)
# Linear regression fits a straight line:
#        y = m x + c
# to experimental data.
#
# scipy.stats.linregress returns:
#   - slope (m)
#   - intercept (c)
#   - r-value (correlation strength)
#
# BEST-FIT LINE:
#   y_fit = m x + c
#
# Plotting the original data points with the fitted line
# shows how well the model matches the data.
#
# CONCEPTS NEEDED:
# - Least squares fitting
# - Correlation and best-fit line
# - Random noise in measurements
# ----------------------------------------------------------
