from src.fetch_data import fetch_earthquake_data
from src.kernel_k_means import KernelKMeans
from src.plot_clusters import plot_clusters
from sklearn.preprocessing import StandardScaler

import numpy as np

def main():
    df = fetch_earthquake_data()
    # 緯度・経度・時間（秒に変換）の特徴量を用意
    df["timestamp"] = df["time"].astype(np.int64) // 10**9 # datetime64型を秒単位に変換
    X = df[["latitude", "longitude", "timestamp"]].to_numpy()

    # 標準化。sklearnライブラリを使用
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # print(X_scaled)

    number_of_clusters = 5 # ここでクラスタ数を定義
    kernel_type = 'rbf' # 'rbf', 'poly'から選択
    model = KernelKMeans(
        n_clusters=number_of_clusters,
        max_iter=100,
        kernel_type=kernel_type,
        kernel_params = {'gamma': 0.01} if kernel_type == 'rbf' else {'coef0': 10.0, 'degree': 5},
    )
    model.fit(X_scaled)

    print("クラスタラベルの分布:", np.bincount(model.labels_))
    print("ユニークなクラスタ数:", len(set(model.labels_)))

    plot_clusters(df, model.labels_, plot_3d=False, save_path=f"results/{kernel_type}_n={number_of_clusters}_2d.png")
    plot_clusters(df, model.labels_, plot_3d=True, save_path=f"results/{kernel_type}_n={number_of_clusters}_3d.png")

if __name__ == "__main__":
    main()