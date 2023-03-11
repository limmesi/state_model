import numpy as np


def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)

    for i in range(n):
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] = U[i + 1:] - factor[:, np.newaxis] * U[i]
    return L, U


# Przypadek I bez ograniczen
print("1.Bez ograniczen")

Q_a = 200
c_a = 2
W_s = 1500
E_12 = 25
Q_b = 300
c_b = 2
E_23 = 50
E_34 = 50
Q_c = 150
E_35 = 25
Q_d = 350
W_g = 2500

L = np.empty([5, 5])
U = np.empty([5, 5])

# 1. Uklad rownan liniowych
A = np.array([[E_12 + Q_a, -E_12, 0, 0, 0],
              [-E_12 - Q_a, E_12 + E_23 + Q_a + Q_b, -E_23, 0, 0],
              [0, -E_23 - Q_a - Q_b, E_23 + E_34 + E_35 + Q_a + Q_b, -E_34, -E_35],
              [0, 0, -E_34 - Q_a - Q_b + Q_d, E_34 + Q_c, 0],
              [0, 0, -E_35 - Q_a - Q_b + Q_c, 0, E_35 + Q_d]])

B = np.array([W_s + Q_a * c_a, Q_b * c_b, 0, 0, W_g])

L, U = lu(A)
# print(U)
# print(L)

inv_L = np.linalg.inv(L)
inv_U = np.linalg.inv(U)

D = np.matmul(inv_L, B)

X = np.matmul(inv_U, D)
print('wynik:')
print(X)

inv_L = np.linalg.inv(L)
inv_U = np.linalg.inv(U)
inv_A = np.dot(inv_U, inv_L)
print('A^(-1)')
print(inv_A)

grill_percantage = 100 * (inv_A[3][4] * W_g) / X[3]
smoker_procentage = 100 * (inv_A[3][0] * W_s) / X[3]
street_procentage = 100 * (inv_A[3][0] * Q_a * c_a + inv_A[3][1] * Q_b * c_b) / X[3]
print("grill: ")
print(grill_percantage)
print("palacze:")
print(smoker_procentage)
print("ulica:")
print(street_procentage)

# Przypadek II Z ograniczeniami
print('2.Z ograniczeniami')
print()
W_s = 800
W_g = 1200

A = np.array([[E_12 + Q_a, -E_12, 0, 0, 0],
              [-E_12 - Q_a, E_12 + E_23 + Q_a + Q_b, -E_23, 0, 0],
              [0, -E_23 - Q_a - Q_b, E_23 + E_34 + E_35 + Q_a + Q_b, -E_34, -E_35],
              [0, 0, -E_34 - Q_a - Q_b + Q_d, E_34 + Q_c, 0],
              [0, 0, -E_35 - Q_a - Q_b + Q_c, 0, E_35 + Q_d]])

B = np.array([W_s + Q_a * c_a, Q_b * c_b, 0, 0, W_g])

L, U = lu(A)
# print(U)
# print(L)

inv_L = np.linalg.inv(L)
inv_U = np.linalg.inv(U)

D = np.matmul(inv_L, B)

X = np.matmul(inv_U, D)
print('wynik:')
print(X)

inv_L = np.linalg.inv(L)
inv_U = np.linalg.inv(U)
inv_A = np.dot(inv_U, inv_L)
print('A^(-1)')
print(inv_A)

grill_percantage = 100 * (inv_A[3][4] * W_g) / X[3]
smoker_procentage = 100 * (inv_A[3][0] * W_s) / X[3]
street_procentage = 100 * (inv_A[3][0] * Q_a * c_a + inv_A[3][1] * Q_b * c_b) / X[3]
print("grill: ")
print(grill_percantage)

print("palacze:")
print(smoker_procentage)

print("ulica:")
print(street_procentage)
