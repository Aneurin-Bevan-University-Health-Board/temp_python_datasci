"""Data loading helpers — BQ, GCS, local."""
from google.cloud import bigquery, storage
import pandas as pd


def load_from_bq(project: str, sql: str) -> pd.DataFrame:
    """Run a BigQuery SQL query and return a DataFrame."""
    client = bigquery.Client(project=project)
    return client.query(sql).to_dataframe()


def load_parquet_from_gcs(bucket: str, blob_path: str) -> pd.DataFrame:
    """Download a Parquet file from GCS and return a DataFrame."""
    client = storage.Client()
    blob = client.bucket(bucket).blob(blob_path)
    data = blob.download_as_bytes()
    import io
    return pd.read_parquet(io.BytesIO(data))
