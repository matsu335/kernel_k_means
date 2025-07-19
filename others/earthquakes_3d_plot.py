# get_earthquakes_3d_plot.py

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.dates as mdates
import datetime

# データ取得
url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query"
    "?format=csv"
    "&starttime=2005-07-01"
    "&endtime=2025-06-30"
    "&minlatitude=24"
    "&maxlatitude=46"
    "&minlongitude=122"
    "&maxlongitude=147"
    "&minmagnitude=5.5"
)
df = pd.read_csv(url)

# time列をdatetime型に変換
df['time'] = pd.to_datetime(df['time'])

# 緯度・経度・日時だけ取り出す
df_subset = df[['time', 'latitude', 'longitude']]

# 3Dプロット
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# X=経度, Y=緯度, Z=時間（数値化）
x = df_subset['longitude']
y = df_subset['latitude']
z = mdates.date2num(df_subset['time'])  # datetime → floatに変換

# プロット
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=5)

# 軸ラベル
ax.set_xlabel("Longitude (経度)")
ax.set_ylabel("Latitude (緯度)")
ax.set_zlabel("Time (日時)")

# Z軸の時系列ラベルを日付として表示
ax.zaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# カラーバー
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label("Date")

# タイトル
plt.title("Japan Earthquakes (M5.5+, 2005–2025) in 3D Space")

plt.tight_layout()
plt.show()
