import numpy as np
from scipy.linalg import lu

Qa = 200
Ca = 2
Ws = 1500
E12 = 25
Qb = 300
Cb = 2
E23 = 50
E35 = 25
E34 = 50
Qc = 150
Qd = 350
Wg = 2500

A = np.array([[Qa+E12, -E12, 0, 0, 0],
              [-E12-Qa, 575, -E34, 0, 0],
              [0, -Qa-Qb-E23, E23+E35+E34+Qa+Qb, -E34, -E35],
              [0, 0, -E34-Qc, Qc+E34, 0],
              [0, 0, -Qd-E35, 0, Qd+E35]])

B = np.array([[Ws + Qa*Ca],
              [Cb*Qb],
              [0],
              [0],
              [Wg]])
# zad 1
A_inv = np.linalg.inv(A)
C_1 = A_inv@B

# zad 2
_, L, U = lu(A)
L_inv = np.linalg.inv(L)
U_inv = np.linalg.inv(U)
C_2 = U_inv@(L_inv@B)

# zad 3

B_new = np.array([[800 + Qa*Ca],
                  [Cb*Qb],
                  [0],
                  [0],
                  [1200]])
C_2_new = U_inv@(L_inv@B_new)

# zad 4

A_inv_2 = np.dot(U_inv, L_inv)

# zad 5
grill = 100 * (A_inv[3][4] * Wg) / C_1[3]
palacze = 100 * (A_inv[3][0] * Ws) / C_1[3]
ulica = 100 * (A_inv[3][0] * Qa * Ca + A_inv[3][1] * Qb * Cb) / C_1[3]

# prezentajca

print(C_1)
print(C_2)
print(C_2_new)
print(A_inv)
print(A_inv_2)
print(grill)
print(palacze)
print(ulica)
