import numpy as np
import matplotlib.pyplot as plt

# Function and exact derivative
def f(x):
    return np.sin(x)

def fprime(x):
    return np.cos(x)

x0 = 1.0   # Point at which derivative is evaluated

# Step sizes (simple list, no logspace)
hs = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

err_left = []
err_right = []
err_central = []

for h in hs:
    left = (f(x0) - f(x0 - h)) / h
    right = (f(x0 + h) - f(x0)) / h
    central = (f(x0 + h) - f(x0 - h)) / (2*h)

    err_left.append(abs(left - fprime(x0)))
    err_right.append(abs(right - fprime(x0)))
    err_central.append(abs(central - fprime(x0)))

# Plot the function and its derivative
x = np.linspace(0, 2*np.pi, 400)
plt.figure()
plt.plot(x, f(x), label="f(x)=sin(x)")
plt.plot(x, fprime(x), label="f'(x)=cos(x)")
plt.xlabel("x")
plt.ylabel("Value")
plt.grid()
plt.legend()
plt.title("Function and Exact Derivative")
plt.show()
plt.savefig("derivative.png")

# Error plot (log-log)
plt.figure()
plt.loglog(hs, err_left, marker='o', label="Left diff")
plt.loglog(hs, err_right, marker='o', label="Right diff")
plt.loglog(hs, err_central, marker='o', label="Central diff")
plt.xlabel("Step size h")
plt.ylabel("Error")
plt.grid(True, which="both")
plt.legend()
plt.title("Error vs Step Size")
plt.show()
plt.savefig("error_log-log.png")


# --------------------------------------------------------------
# THEORY (BRIEF)
# Numerical derivative approximations:
#   Left:    f'(x) ≈ (f(x)   - f(x-h)) / h
#   Right:   f'(x) ≈ (f(x+h) - f(x))   / h
#   Central: f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
#
# Central difference is most accurate (error ~ h²).
# Left and right have error ~ h.
#
# ERROR BEHAVIOUR:
# As h decreases:
#   - truncation error decreases
#   - round-off error increases (for very small h)
#
# CONCEPTS NEEDED:
# - Taylor series
# - Numerical error
# - Log-log plotting
# - Floating point precision limits
# --------------------------------------------------------------
