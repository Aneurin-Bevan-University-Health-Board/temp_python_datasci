import pandas as pd
from src.features.engineering import add_date_features


def test_add_date_features():
    df = pd.DataFrame({"date": ["2024-01-01", "2024-06-15"]})
    result = add_date_features(df, "date")
    assert "date_year" in result.columns
    assert "date_is_weekend" in result.columns
    assert result["date_year"].iloc[0] == 2024
