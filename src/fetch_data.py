import pandas as pd

def fetch_earthquake_data():
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
    df_subset = df[["time", "latitude", "longitude"]].copy() # 日時、緯度、経度の情報を取得
    df_subset["time"] = pd.to_datetime(df_subset["time"]) # pandasを使い、str型をdatetime64型に変換
    return df_subset