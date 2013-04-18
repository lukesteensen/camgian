import numpy as np
import pandas as pd

rng = pd.date_range('10/1/2012', '4/19/2013', freq='3D').astype(np.int64) // 10**6

def ts():
    return pd.ewma(pd.Series(np.random.randn(len(rng)), index=rng), span=20)

def get_data(series):
    data = [[int(x[0]), x[1]] for x in zip(series.index.tolist(), series.values)]
    return {
        'data': data,
        'min': int(series.min()),
        'max': int(series.max()),
        'avg': int(series.mean()),
    }

def level_data():
    series = ts() * 500 + 500
    series = series.clip(0, 800)
    data = get_data(series)
    data['low_alarm'] = int(series.max() * 0.70)
    data['high_alarm'] = int(series.max() * 0.30)
    return data

def temp_data():
    series = ts() * 50 + 50
    series = series.clip(0, 800)
    return get_data(series)

