import numpy as np
from src.kernel_func import rbf_kernel, polynomial_kernel

class KernelKMeans:
    def __init__(self, n_clusters=3, kernel_type='rbf', max_iter=100, kernel_params=None):
        self.n_clusters = n_clusters # 分類するクラスタ数
        self.kernel_type = kernel_type # カーネルの種類
        self.max_iter = max_iter # 最大反復回数
        self.kernel_params = kernel_params or {}

    def _get_kernel(self, X):
        if self.kernel_type == 'rbf':
            return rbf_kernel(X, **self.kernel_params)
        elif self.kernel_type == 'poly':
            return polynomial_kernel(X, **self.kernel_params)
        else:
            raise ValueError(f"Unknown kernel type: {self.kernel_type}")

    def fit(self, X):
        n_samples = X.shape[0] # データ数N

        # カーネルを定義
        K = self._get_kernel(X)
        # K = polynomial_kernel(X, degree=3, coef0=1.0)

        labels = np.random.randint(self.n_clusters, size=n_samples) # 最初はランダムにクラスタラベルを付与
        # print(labels)

        step = 0
        for _ in range(self.max_iter):
            distance = np.zeros((n_samples, self.n_clusters)) # 各サンプルの、各クラスタの代表点との距離を定義
            for j in range(self.n_clusters):
                mask = labels == j # 現在クラスタjに属するデータ点のブールマスクを作成
                denom = np.sum(mask) # クラスタjに属するデータ点の数を計算
                if denom == 0:
                    # 空クラスタの場合、ランダムに1点だけこのクラスタに割り当てて復活させる
                    random_index = np.random.choice(n_samples)
                    labels[random_index] = j
                    mask = labels == j
                    denom = np.sum(mask)

                # 特徴空間における距離を計算
                K_ij = K[:, mask]
                K_jj = K[np.ix_(mask, mask)]
                distance[:, j] = np.diag(K) - 2 * np.sum(K_ij, axis=1) / denom + np.sum(K_jj) / (denom ** 2)

            # 各パターンを最短距離のクラスタに割り当てる
            new_labels = np.argmin(distance, axis=1)
            step += 1
            if np.all(labels == new_labels):
                print(f"labeling finished. number of step: {step}")
                break # パターンへのクラスタの割り当ての変化が収束したら終了
            labels = new_labels
            # print(labels)

        self.labels_ = labels
        self.K_ = K
        return self