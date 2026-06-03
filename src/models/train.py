"""Model training scaffold with MLflow tracking."""
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def train_and_log(model, X, y, run_name: str = "run", test_size: float = 0.2):
    """Train a sklearn-compatible model and log to MLflow."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    with mlflow.start_run(run_name=run_name):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        report = classification_report(y_test, preds, output_dict=True)
        mlflow.log_metric("accuracy", report["accuracy"])
        mlflow.sklearn.log_model(model, artifact_path="model")

        print(classification_report(y_test, preds))
        return model
