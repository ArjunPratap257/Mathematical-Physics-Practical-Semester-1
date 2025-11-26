import numpy as np

c = 3e8

x = float(input("Enter x: "))
t = float(input("Enter t: "))
v = float(input("Enter velocity v: "))

# Galilean
x_g = x - v*t
t_g = t
print("Galilean:", x_g, t_g)

# Lorentz
if abs(v) < c:
    gamma = 1/np.sqrt(1 - (v/c)**2)
    x_l = gamma*(x - v*t)
    t_l = gamma*(t - (v*x)/c**2)
    print("Lorentz:", x_l, t_l)
else:
    print("Lorentz invalid (v >= c)")

# Rotation
x2 = float(input("Enter x for rotation: "))
y2 = float(input("Enter y for rotation: "))
angle = float(input("Angle (degrees): "))

theta = np.radians(angle)
xr = x2*np.cos(theta) - y2*np.sin(theta)
yr = x2*np.sin(theta) + y2*np.cos(theta)

print("Rotation:", xr, yr)

# ----------------------------------------------------------
# THEORY (BRIEF)
# 1) GALILEAN TRANSFORMATION (Classical mechanics)
#    x' = x - v t
#    t' = t
#    Valid when v << c (low speeds).
#
# 2) LORENTZ TRANSFORMATION (Special relativity)
#    x' = γ (x - v t)
#    t' = γ (t - v x / c²)
#    where γ = 1 / sqrt(1 - v²/c²)
#    Required when v is comparable to the speed of light.
#
# 3) ROTATION TRANSFORMATION (2D rotation)
#    x' = x cosθ - y sinθ
#    y' = x sinθ + y cosθ
#    Used for rotating coordinate systems.
#
# CONCEPTS NEEDED:
# - Inertial reference frames
# - Speed of light limit
# - Time dilation & length contraction
# - Rotation matrices
# ----------------------------------------------------------
