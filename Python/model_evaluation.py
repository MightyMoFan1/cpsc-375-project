import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)


def validate_data(actual: np.ndarray, predicted: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Validate shape, dimensionality, and finiteness of inputs."""
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)

    if actual.shape != predicted.shape:
        raise ValueError("Actual and predicted values must have the same shape.")
    if actual.size == 0:
        raise ValueError("Input arrays cannot be empty.")
    if actual.ndim != 1:
        raise ValueError("Input arrays must be one-dimensional.")
    if not np.all(np.isfinite(actual)):
        raise ValueError("Actual values must contain only finite elements.")
    if not np.all(np.isfinite(predicted)):
        raise ValueError("Predicted values must contain only finite elements.")

    return actual, predicted


def calculate_metrics(actual: np.ndarray, predicted: np.ndarray) -> dict[str, float]:
    """Compute standard statistical metrics evaluating predicted against actual data."""
    actual, predicted = validate_data(actual, predicted)

    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(actual, predicted)
    mape = np.nan if np.any(actual == 0) else mean_absolute_percentage_error(actual, predicted) * 100
    r2 = np.nan if len(actual) < 2 else r2_score(actual, predicted)

    return {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "MAPE (%)": mape,
        "R2": r2
    }


def calculate_residuals(actual: np.ndarray, predicted: np.ndarray) -> np.ndarray:
    """Calculate raw residual values (Actual - Predicted)."""
    actual, predicted = validate_data(actual, predicted)
    return actual - predicted


def display_metrics(metrics: dict[str, float]) -> None:
    """Format and print computed regression evaluation metrics to console."""
    print("\nMODEL EVALUATION RESULTS")
    print("-" * 24)
    for metric, value in metrics.items():
        if np.isnan(value):
            print(f"{metric:<10}: Not defined")
        else:
            print(f"{metric:<10}: {value:.6f}")


def plot_residuals(actual: np.ndarray, predicted: np.ndarray) -> None:
    """Generate a clean residual scatter plot against actual target values."""
    actual, predicted = validate_data(actual, predicted)
    residuals = calculate_residuals(actual, predicted)

    plt.figure(figsize=(9, 5))
    plt.scatter(actual, residuals, color="#3182bd", alpha=0.8, edgecolors="w", s=60, zorder=3)
    plt.axhline(y=0, color="#e06666", linestyle="--", linewidth=1.5, zorder=2)

    plt.title("Residual Analysis Plot", fontsize=14, pad=15)
    plt.xlabel("Actual Target Values", fontsize=11)
    plt.ylabel("Residuals (Actual - Predicted)", fontsize=11)
    plt.grid(True, linestyle=":", alpha=0.6, zorder=1)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Sample evaluation dataset
    y_true = np.array([100, 150, 200, 250, 300])
    y_pred = np.array([110, 145, 190, 260, 290])

    # Run computations
    metrics_results = calculate_metrics(y_true, y_pred)
    residual_values = calculate_residuals(y_true, y_pred)

    # Deliver outputs
    display_metrics(metrics_results)
    print("\nRESIDUALS")
    print("-" * 9)
    print(residual_values)

    plot_residuals(y_true, y_pred)
