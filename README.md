# カーネル k-means による日本周辺の地震データのクラスタリング

> **実施時期:** 2025年7月
> **README 整理:** 2026年10月25日（就職活動での公開にあたり、README.md の整理のみを行いました。コードは実験当時のまま変更していません）

## 概要

日本周辺で起きた地震を、震源の位置（緯度・経度）と発生時刻をもとにクラスタリングしました。手法には **カーネル k-means を自前で実装**して用いています。

- **データ:** USGS（アメリカ地質調査所）の地震カタログから、日本周辺（北緯 24〜46°、東経 122〜147°）で 2005年7月〜2025年6月に起きた M5.5 以上の地震を取得
- **特徴量:** 緯度・経度・発生時刻の 3 つを標準化したもの
- **手法:** カーネル k-means（[src/kernel_k_means.py](src/kernel_k_means.py)）
  - scikit-learn の KMeans は使わず、カーネル行列から特徴空間でのクラスタ中心との距離を計算する処理を実装
  - カーネルは RBF カーネルと多項式カーネルから選択可能
  - ラベルの割り当てが変わらなくなった時点で収束とし、空のクラスタができた場合はランダムに 1 点を割り当てて復活させる
- **可視化:** クラスタリングの結果を、緯度・経度の 2D 散布図と、時刻を加えた 3D 散布図で出力

考察などの詳細はレポートにまとめています。

## 使用技術

- Python
- NumPy（カーネル k-means の実装）
- pandas（データ取得・整形）
- matplotlib（可視化）
- scikit-learn（標準化と距離計算のみ）

## ディレクトリ構成

```
kernel_k_means/
├── main.py                    # メイン実行ファイル（データ取得 → クラスタリング → 可視化）
├── src/
│   ├── fetch_data.py          # USGS から地震データを取得
│   ├── kernel_func.py         # RBF カーネル・多項式カーネル
│   ├── kernel_k_means.py      # カーネル k-means の実装
│   └── plot_clusters.py       # 結果の可視化（2D / 3D）
├── others/
│   ├── earthquakes_3d_plot.py # 地震データを 3D 表示するだけのスクリプト（本体では未使用）
│   └── japan_map.png          # 緯度・経度に合わせた日本地図
└── requirements.txt
```

## 実行方法

リポジトリのルートで実行します。地震データは実行時に USGS の API から取得するため、インターネット接続が必要です。

```bash
pip install -r requirements.txt
python main.py
```

結果の画像は `results/` に保存されます（例: `results/rbf_n=5_2d.png`、`results/rbf_n=5_3d.png`）。

### パラメータの変更

`main.py` の次の変数を書き換えます。

| 変数 | 内容 |
|---|---|
| `number_of_clusters` | クラスタ数（初期値: 5） |
| `kernel_type` | `'rbf'`（RBF カーネル）または `'poly'`（多項式カーネル） |
| `kernel_params` | カーネルのパラメータ。RBF は `gamma`、多項式は `coef0` と `degree` |

## データについて

地震データは [USGS Earthquake Catalog](https://earthquake.usgs.gov/fdsnws/event/1/) の API から取得しています。

## 利用について

本リポジトリは、ポートフォリオとして閲覧していただくことを目的に公開しています。コードの無断転載・再利用はご遠慮ください。
