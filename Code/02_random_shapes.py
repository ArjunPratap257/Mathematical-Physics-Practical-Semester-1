import random
import math

# Random dimensions
r = random.uniform(1, 10)        # radius
l = random.uniform(1, 20)        # length
w = random.uniform(1, 20)        # width
h = random.uniform(1, 20)        # height

# Calculations
circle_area = math.pi * r * r
rectangle_area = l * w
sphere_volume = (4/3) * math.pi * r**3
cuboid_volume = l * w * h

# Output
print("Random radius =", r)
print("Area of circle =", circle_area)

print("\nRandom length =", l, "width =", w)
print("Area of rectangle =", rectangle_area)

print("\nRandom radius for sphere =", r)
print("Volume of sphere =", sphere_volume)

print("\nRandom length =", l, "width =", w, "height =", h)
print("Volume of cuboid =", cuboid_volume)

# ----------------------------------------------------------
# THEORY (BRIEF)
# Random.uniform(a,b) generates a random decimal in [a,b].
# We use basic geometry formulas:
#  - Circle area       = π r²
#  - Rectangle area    = l × w
#  - Sphere volume     = (4/3) π r³
#  - Cuboid volume     = l × w × h
#
# CONCEPTS NEEDED:
# - Random number generation in Python
# - Geometry formulas (area & volume)
# - Use of math.pi
# - Understanding floating-point numbers
# ----------------------------------------------------------
