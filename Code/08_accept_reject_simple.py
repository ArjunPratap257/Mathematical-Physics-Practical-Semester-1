import numpy as np

rng = np.random.default_rng()

# Estimating pi
N = int(input("Enter N for pi estimation: "))
x = rng.uniform(0,1,N)
y = rng.uniform(0,1,N)
pi_est = 4 * np.sum(x*x + y*y <= 1) / N
print("Estimated pi =", pi_est)

# Integrating sin(x) from 0 to pi
M = int(input("Enter N for integration: "))
x2 = rng.uniform(0, np.pi, M)
y2 = rng.uniform(0, 1, M)
integral = np.sum(y2 <= np.sin(x2)) / M * np.pi
print("Integral of sin(x) from 0 to pi =", integral)

# ----------------------------------------------------------
# THEORY (BRIEF)
# Acceptance–rejection Monte Carlo:
#
# 1) Estimating π:
#    - Generate random (x,y) in the unit square [0,1]×[0,1].
#    - Count how many satisfy x² + y² ≤ 1 (inside quarter circle).
#    - π ≈ 4 × (points inside / total points).
#
# 2) Numerical Integration:
#    For integral ∫ f(x) dx over [a,b]:
#    - Sample x uniformly in [a,b].
#    - Sample y uniformly in [0, f_max].
#    - Accept if y ≤ f(x).
#    - Integral ≈ (accepted / total) × (b–a) × f_max.
#
# In this program:
#    f(x) = sin(x), a = 0, b = π, f_max = 1
#
# CONCEPTS NEEDED:
# - Monte Carlo random sampling
# - Area estimation by point counting
# - Acceptance–rejection logic
# - Probabilistic numerical integration
# ----------------------------------------------------------
