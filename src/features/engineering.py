"""Feature engineering utilities."""
import pandas as pd
import numpy as np


def add_date_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Expand a date column into year, month, day_of_week, is_weekend features."""
    df = df.copy()
    dt = pd.to_datetime(df[date_col])
    df[f"{date_col}_year"] = dt.dt.year
    df[f"{date_col}_month"] = dt.dt.month
    df[f"{date_col}_dow"] = dt.dt.dayofweek
    df[f"{date_col}_is_weekend"] = (dt.dt.dayofweek >= 5).astype(int)
    return df
