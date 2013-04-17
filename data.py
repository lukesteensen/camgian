import numpy as np
import pandas as pd

def fake_series():
    rng = pd.date_range('10/1/2012', '4/19/2013', freq='3D').astype(np.int64) // 10**6
    ts = pd.ewma(pd.Series(np.random.randn(len(rng)), index=rng), span=20)
    ts = ts * 500 + 500
    ts = ts.clip(0, 800)
    return [[int(x[0]), x[1]] for x in zip(ts.index.tolist(), ts.values)]

