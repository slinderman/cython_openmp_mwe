# Cythonized version of sum anti diag
#
# distutils: extra_compile_args = -O3 -fopenmp
# distutils: extra_link_args = -fopenmp
# cython: wraparound=False
# cython: boundscheck=False
# cython: nonecheck=False
# cython: cdivision=False


import numpy as np
cimport numpy as np

from cython cimport floating
from cython.parallel import prange

cpdef sum_anti_diag(floating[:,:,::1] A):
    """
    Sum the anti-diagonal of a stack of square matrices.
    This is a special case of Ton's code.

    :param A:  3D array of shape (N, K, K)
    :return B: 2D output array of shape (N, 2K-1)
               where B[n,k] = sum_{j=0}^k A[n,k-j,j] for k <= K
               and   B[n,K+k-1] = sum_{j=0}^{K-k-1} A[n,k+j,K-1-j] for k < K
    """

    cdef int n,j,k,k2
    cdef int N, K
    N = A.shape[0]
    K = A.shape[1]
    assert A.shape[2] == K

    # Initialize output
    cdef double[:, ::1] B = np.zeros((N, 2*K-1))

    # Parallel loop over N
    with nogil:
        for n in prange(N):
            # First K entries
            for k in range(K):
                for j in range(k+1):
                    B[n,k] += A[n,k-j,j]

            # Second K-1 entries
            # e.g. A[1,K] + A[2,K-1] + A[3, K-2] + ... + A[K-1,1]
            for k in range(1,K):
                for j in range(K-k):
                    B[n,K+k-1] += A[n,k+j,K-1-j]

    return np.asarray(B)
