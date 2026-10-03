import numpy as np

y = np.array([0, 2, 4, 6, 8, 10, 12, 14])
H = np.array([0, 1, 1.5, 3, 3.5, 3.2, 2, 0])
U = np.array([0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0])

h = y[1] - y[0]


A_trap = h * (0.5*H[0] + np.sum(H[1:-1]) + 0.5*H[-1])

HU = H * U
Q_trap = h * (0.5*HU[0] + np.sum(HU[1:-1]) + 0.5*HU[-1])

U_trap = Q_trap / A_trap

A_1 = (h/3) * (H[0] + H[4] +
                4*(H[1] + H[3]) +
                2*H[2])

A_2 = (3*h/8) * (H[4] + H[7] +
                  3*(H[5] + H[6]))

A_simp = A_1 + A_2


Q_1 = (h/3) * (HU[0] + HU[4] +
                4*(HU[1] + HU[3]) +
                2*HU[2])

Q_2 = (3*h/8) * (HU[4] + HU[7] +
                  3*(HU[5] + HU[6]))

Q_simp = Q_1 + Q_2


U_simp = Q_simp / A_simp

print("              Trapezoidal       Simpson")
print("Area (m^2)     ", A_trap, "        ", A_simp)
print("Discharge      ", Q_trap, "        ", Q_simp)
print("Avg velocity   ", U_trap, "        ", U_simp)