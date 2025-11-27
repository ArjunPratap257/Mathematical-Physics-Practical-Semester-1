import numpy as np
import matplotlib.pyplot as plt

g = 9.8

u = float(input("Enter speed (m/s): "))
theta = float(input("Enter angle (degrees): "))

# Total time of flight
T = 2 * u * np.sin(np.radians(theta)) / g

# Time array
t = np.linspace(0, T, 400)

# Motion equations
x = u * np.cos(np.radians(theta)) * t
y = u * np.sin(np.radians(theta)) * t - 0.5 * g * t**2

# Outputs
print("Time of flight =", T)
print("Range =", x[-1])
print("Maximum height =", max(y))

# Plot
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Motion")
plt.grid()
plt.show()
plt.savefig("../plots/projectile.png")

# ----------------------------------------------------------
# THEORY (BRIEF)
# A projectile moves under gravity with no air resistance.
# Equations used:
#    x(t) = u cosθ · t
#    y(t) = u sinθ · t − ½ g t²
#
# Time of flight:  T = 2u sinθ / g
# Range:           R = u² sin(2θ) / g
# Maximum height:  H = (u² sin²θ) / (2g)
#
# CONCEPTS NEEDED:
# - Resolving velocity into components
# - Kinematics equations
# - Parabolic trajectory
# - Basic trigonometry (sin, cos)
# ----------------------------------------------------------
