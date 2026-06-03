# Python Data Science Template

Full data science starter for ABUHB. High-power Codespaces devcontainer with the complete ML/stats stack plus GCP tooling.

**Use this when:** you're building models, running statistical analysis, doing experimentation, or producing reproducible research.

---

## Quick Start

1. Click **Use this template** → create your repo
2. Open in GitHub Codespaces — the devcontainer requests a **16-core / 64GB** machine automatically
3. Authenticate with GCP (see [GCP Login](#gcp-login))
4. Start in `notebooks/` for exploration or `src/` for production code

---

## Folder Structure

```
.
├── .devcontainer/       # High-power Codespaces config
├── src/
│   ├── data/            # Data loading and preprocessing
│   ├── features/        # Feature engineering
│   ├── models/          # Model training and evaluation
│   └── utils/           # Shared helpers
├── notebooks/
│   ├── exploratory/     # EDA — not production
│   └── reports/         # Finalised analysis notebooks
├── tests/
├── data/                # Local data (gitignored)
├── models/              # Saved model artefacts (gitignored)
├── requirements.txt
└── .env.example
```

---

## GCP Login

### Option 1 — Application Default Credentials (recommended for Codespaces)

```bash
gcloud auth application-default login
```

### Option 2 — Service Account Key (CI / non-interactive)

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
```

Never commit keys. Use Secret Manager or GitHub Secrets.

### Verify

```bash
gcloud auth list
gcloud config get-value project
```

---

## Stack

### Data & Wrangling
| Library | Purpose |
|---------|---------|
| `pandas` | DataFrames |
| `polars` | Fast DataFrames for large data |
| `numpy` | Numerical computing |
| `pyarrow` | Parquet / Arrow columnar |
| `dask` | Out-of-core / parallel DataFrames |

### ML & Stats
| Library | Purpose |
|---------|---------|
| `scikit-learn` | Classical ML |
| `statsmodels` | Statistical modelling, regression, time series |
| `scipy` | Scientific computing, statistical tests |
| `xgboost` | Gradient boosting |
| `lightgbm` | Fast gradient boosting |
| `shap` | Model explainability |

### Experiment Tracking
| Library | Purpose |
|---------|---------|
| `mlflow` | Experiment tracking, model registry |

### Visualisation
| Library | Purpose |
|---------|---------|
| `matplotlib` | Core plotting |
| `seaborn` | Statistical visualisation |
| `plotly` | Interactive charts |

### GCP
| Library | Purpose |
|---------|---------|
| `google-cloud-bigquery` | BigQuery |
| `google-cloud-storage` | GCS |
| `google-cloud-aiplatform` | Vertex AI |
| `google-cloud-secret-manager` | Secrets |

---

## GCP Usage

### BigQuery
```python
from google.cloud import bigquery
client = bigquery.Client(project="your-gcp-project")
df = client.query("SELECT * FROM `project.dataset.table`").to_dataframe()
```

### Cloud Storage
```python
from google.cloud import storage
client = storage.Client()
client.bucket("your-bucket").blob("file.parquet").download_to_filename("local.parquet")
```

### Secret Manager
```python
from google.cloud import secretmanager
client = secretmanager.SecretManagerServiceClient()
name = "projects/your-project/secrets/your-secret/versions/latest"
value = client.access_secret_version(request={"name": name}).payload.data.decode()
```

### Vertex AI
```python
from google.cloud import aiplatform
aiplatform.init(project="your-gcp-project", location="europe-west2")
```

---

## Reproducibility

- Pin all dependencies in `requirements.txt`
- Log all experiments with MLflow: `mlflow.start_run()`
- Store trained models in GCS or Vertex AI Model Registry
- Use `notebooks/reports/` only for finalised, reproducible notebooks

---

## Running Tests

```bash
pytest tests/ --cov=src
```
