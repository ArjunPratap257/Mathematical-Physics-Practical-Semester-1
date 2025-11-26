def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

m = int(input("Enter red balls: "))
n = int(input("Enter blue balls: "))

ways = factorial(m + n) // (factorial(m) * factorial(n))
print("Ways =", ways)

# ------------------------------------------------------
# THEORY (BRIEF)
# Factorial n! = 1 × 2 × 3 × ... × n.
# Arranging m red + n blue indistinguishable balls is a
# COMBINATION problem:
#     Number of arrangements = (m+n)! / (m! n!)
#
# CONCEPTS NEEDED:
# - Factorials
# - Combinations
# - Permutations of identical objects
# ------------------------------------------------------
