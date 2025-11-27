import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# Choose sample sizes
Ns = [500, 2000, 10000]

for N in Ns:
    plt.hist(rng.uniform(0,1,N), bins=30)
    plt.title(f"Uniform, N={N}")
    plt.show()

    plt.hist(rng.binomial(10,0.5,N), bins=30)
    plt.title(f"Binomial, N={N}")
    plt.show()

    plt.hist(rng.poisson(4,N), bins=30)
    plt.title(f"Poisson, N={N}")
    plt.show()

    plt.hist(rng.normal(0,1,N), bins=30)
    plt.title(f"Gaussian, N={N}")
    plt.show()

# Central Limit Theorem
data = rng.uniform(0,1,(100000,10))
means = np.mean(data, axis=1)

plt.hist(means, bins=50, density=True)
plt.title("Central Limit Theorem")
plt.show()
plt.savefig("../plots/random_distribution.png")


# ----------------------------------------------------------
# THEORY (BRIEF)
# Uniform: every value equally likely in an interval.
# Binomial: number of successes in repeated trials.
# Poisson: counts of rare events in a fixed interval.
# Gaussian: continuous bell curve.
#
# As N increases, histograms match theoretical shapes
# → Law of Large Numbers.
#
# CENTRAL LIMIT THEOREM:
# Average of many random variables tends to a Gaussian,
# regardless of the original distribution.
#
# CONCEPTS NEEDED:
# - Random sampling
# - Histograms
# - Probability distributions
# - Law of large numbers
# - Central Limit Theorem (CLT)
# ----------------------------------------------------------
