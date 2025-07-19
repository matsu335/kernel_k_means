import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def rbf_kernel(X, Y=None, gamma=None):
    """
    RBF (Gaussian) カーネル: K(x, y) = exp(-γ ||x - y||²)
    """
    if Y is None:
        Y = X

    if gamma is None:
        gamma = 1.0 / X.shape[1]

    dists = euclidean_distances(X, Y, squared=True) # ユークリッド距離を計算。sklearnライブラリを使用
    K = np.exp(-gamma * dists)

    return K

def polynomial_kernel(X, Y=None, degree=3, coef0=1.0):
    """
    多項式カーネル: K(x, y) = (xᵀy + coef0)^degree
    """
    if Y is None:
        Y = X
    return (np.dot(X, Y.T) + coef0) ** degree
