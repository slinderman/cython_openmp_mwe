import numpy as np
from cython_sum_anti_diag import sum_anti_diag


def manual_sum_anti_diag(A):
    N, K, _ = A.shape
    B = np.zeros((N, 2*K - 1))
    for n in range(N):
        Anf = np.fliplr(A[n])
        for i,k in enumerate(range(K-1, -K, -1)):
            B[n,i] = np.sum(np.diag(Anf, k))

    return B


if __name__ == "__main__":

    # Simple test
    K = 3
    A = np.arange(K ** 2, dtype=np.double).reshape((1, K, K))

    print("A:\n", A[0])
    print("Af:\n", np.fliplr(A[0]))

    B_manual = manual_sum_anti_diag(A)
    B_cython = sum_anti_diag(A)
    print("simple: cython = manual? ", np.allclose(B_manual, B_cython))
    assert np.allclose(B_manual, B_cython)

    # Harder test
    N = 10
    K = 3
    A = np.random.randn(N, K, K)

    B_manual = manual_sum_anti_diag(A)
    B_cython = sum_anti_diag(A)
    print("harder: cython = manual? ", np.allclose(B_manual, B_cython))
    assert np.allclose(B_manual, B_cython)



