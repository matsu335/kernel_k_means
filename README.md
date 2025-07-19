・ファイル構造
kernel_k_means/
├── k_env/                       ← 仮想環境
├── others/
│   ├── earthquakes_3d_plot.py   ← 地震データ可視化(使わない)
│   └── japan_map.png         ← 緯度・経度を反映した日本地図
├── results/                     ← 結果保存用
├── src/
│   ├── fetch_data.py            ← 地震データ取得スクリプト
│   ├── kernel_func.py           ← カーネルを定義
│   ├── kernel_k_means.py        ← カーネルk-means実装
│   └── plot_clusters.py         ← 結果可視化
├── main.py                      ← メイン実行ファイル
├── requirements.txt             ← 必要パッケージ
└── README.md

・実行方法
1. 仮想環境に入る（もしくはrequirements.txt内のライブラリをインストール）
2. kernel_k_meansディレクトリで「python main.py」を実行
3. results内に結果のpngが保存される

・パラメータ変更方法
number_of_clusters(in main.py): 分類するクラスタの数を設定
kernel_type(in main.py): 用いるカーネルの種類を変更
kernel_params(in main.py): カーネルのパラメータを変更。gamma→rbfカーネル用。coef0, degree→多項式カーネル用。