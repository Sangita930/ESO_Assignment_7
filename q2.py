import math

def Q(t):
    return 8 + 5 * math.cos(0.4 * t)**2

def c(t):
    return 5 * math.exp(-0.5 * t) + 3 * math.exp(0.15 * t)

def f(t):
    return Q(t) * c(t)

a = 2
b = 8
tol = 0.1

R = []

for k in range(10):

    n = 2**k
    h = (b - a) / n

    T = h * (0.5 * f(a) + 0.5 * f(b))

    for i in range(1, n):
        T += h * f(a + i * h)

    row = [T]

    for j in range(1, k + 1):
        value = row[j - 1] + (
            row[j - 1] - R[k - 1][j - 1]
        ) / (4**j - 1)

        row.append(value)

    R.append(row)

    if k > 0:
        error = abs(
            (R[k][k] - R[k - 1][k - 1]) / R[k][k]
        ) * 100

        if error < tol:
            break

print("Romberg Table:")

for i, row in enumerate(R):
    print(i, end="  ")
    for value in row:
        print(f"{value:.6f}", end="  ")
    print()


M = R[-1][-1]

print("\nMass transported =", M, "mg")
print("Relative error =", error, "%")