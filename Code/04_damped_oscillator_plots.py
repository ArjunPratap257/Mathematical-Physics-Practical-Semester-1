import numpy as np
import matplotlib.pyplot as plt

m = 1.0
k = 1.0
omega0 = np.sqrt(k/m)

t = np.linspace(0, 20, 1000)
x0 = 1.0
v0 = 0.0

def damped_motion(zeta, t, x0, v0):
    if zeta < 1:
        omega_d = omega0 * np.sqrt(1 - zeta**2)
        A = x0
        B = (v0 + zeta*omega0*x0)/omega_d
        x = np.exp(-zeta*omega0*t) * (A*np.cos(omega_d*t) + B*np.sin(omega_d*t))
    elif zeta == 1:
        A = x0
        B = v0 + omega0*x0
        x = (A + B*t) * np.exp(-omega0*t)
    else:
        r1 = -omega0*(zeta - np.sqrt(zeta**2 - 1))
        r2 = -omega0*(zeta + np.sqrt(zeta**2 - 1))
        A = (v0 - r2*x0)/(r1 - r2)
        B = (r1*x0 - v0)/(r1 - r2)
        x = A*np.exp(r1*t) + B*np.exp(r2*t)
    return x

cases = {
    "Undamped (ζ=0)": 0.0,
    "Underdamped (ζ=0.2)": 0.2,
    "Critically damped (ζ=1)": 1.0,
    "Overdamped (ζ=2)": 2.0,
}

plt.figure(figsize=(10, 6))
for label, zeta in cases.items():
    x = damped_motion(zeta, t, x0, v0)
    plt.plot(t, x, label=label)

plt.title("Damped Harmonic Oscillator")
plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t)")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("../plots/damping.png")


# ----------------------------------------------------------
# THEORY (BRIEF)
# The damped harmonic oscillator satisfies:
#       x'' + 2ζω₀ x' + ω₀² x = 0
#
# ζ = damping ratio:
#   ζ = 0      → Undamped, oscillatory motion.
#   0 < ζ < 1  → Underdamped, decaying oscillations.
#   ζ = 1      → Critically damped, fastest non-oscillatory return to equilibrium.
#   ζ > 1      → Overdamped, slow exponential return without oscillation.
#
# Solutions:
# Undamped:          x = x₀ cos(ω₀ t)
# Underdamped:       x = e^{-ζω₀t}[A cos(ω_d t) + B sin(ω_d t)],  ω_d = ω₀ sqrt(1–ζ²)
# Critically damped: x = (A + Bt) e^{-ω₀ t}
# Overdamped:        x = C₁ e^{r₁ t} + C₂ e^{r₂ t} (real exponents)
#
# CONCEPTS NEEDED:
# - Damping ratio ζ
# - Natural frequency ω₀
# - Exponential decay
# - Oscillatory vs non-oscillatory motion
# - Second-order ODE solutions
# ----------------------------------------------------------
