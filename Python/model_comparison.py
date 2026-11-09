import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)


def discrete_logistic_growth(
    p0: float, r: float, k: float, iterations: int
) -> np.ndarray:
    """Calculate population over time using the discrete logistic growth model."""
    population = np.zeros(iterations + 1)
    population[0] = p0

    for n in range(iterations):
        population[n + 1] = population[n] + r * population[n] * (
            1 - population[n] / k
        )

    return population


def continuous_logistic_growth(
    t: float, p: np.ndarray, r: float, k: float
) -> float:
    """Differential equation for the continuous logistic growth model."""
    return r * p * (1 - p / k)


def simulate_continuous(
    p0: float, r: float, k: float, time_points: np.ndarray
) -> np.ndarray:
    """Solve the continuous logistic differential equation over given time points."""
    solution = solve_ivp(
        continuous_logistic_growth,
        t_span=[time_points[0], time_points[-1]],
        y0=[p0],
        t_eval=time_points,
        rtol=1e-9,
        atol=1e-11,
        args=(r, k),
    )

    if not solution.success:
        raise RuntimeError(f"ODE Solver failed: {solution.message}")

    return solution.y[0]


# ==========================================
# Simulation Setup & Execution
# ==========================================
P0 = 10.0
R = 0.5
K = 100.0
ITERATIONS = 50

# Generate time frameworks
discrete_time = np.arange(ITERATIONS + 1)
continuous_time = np.linspace(0, ITERATIONS, 501)

# Run simulations
discrete_pop = discrete_logistic_growth(P0, R, K, ITERATIONS)
continuous_pop_dense = simulate_continuous(P0, R, K, continuous_time)
continuous_pop_integers = simulate_continuous(P0, R, K, discrete_time)

# ==========================================
# Metric Calculations
# ==========================================
abs_diff = np.abs(discrete_pop - continuous_pop_integers)
mse = mean_squared_error(discrete_pop, continuous_pop_integers)
rmse = np.sqrt(mse)
mae = mean_absolute_error(discrete_pop, continuous_pop_integers)
mape = mean_absolute_percentage_error(discrete_pop, continuous_pop_integers) * 100
r2 = r2_score(discrete_pop, continuous_pop_integers)

# ==========================================
# Console Output Formatting
# ==========================================
print("\nDISCRETE VS. CONTINUOUS LOGISTIC MODEL")
print("-" * 38)
print(f"Initial Population : {P0}")
print(f"Growth Rate        : {R}")
print(f"Carrying Capacity  : {K}")
print(f"Iterations         : {ITERATIONS}")

print("\nFINAL POPULATION")
print("-" * 16)
print(f"Discrete           : {discrete_pop[-1]:.6f}")
print(f"Continuous         : {continuous_pop_integers[-1]:.6f}")

print("\nMODEL COMPARISON METRICS")
print("-" * 24)
print(f"MSE                : {mse:.6f}")
print(f"RMSE               : {rmse:.6f}")
print(f"MAE                : {mae:.6f}")
print(f"MAPE               : {mape:.6f}%")
print(f"R²                 : {r2:.6f}\n")

# ==========================================
# Visualization & Plotting
# ==========================================
# Plot 1: Model Comparison
plt.figure(figsize=(10, 6))
plt.plot(
    discrete_time,
    discrete_pop,
    "o-",
    markersize=4,
    label="Discrete Logistic Model",
)
plt.plot(
    continuous_time,
    continuous_pop_dense,
    linewidth=2,
    label="Continuous Logistic Model",
)
plt.axhline(
    y=K, color="r", linestyle="--", alpha=0.7, label=f"Carrying Capacity ({K})"
)

plt.title("Discrete vs. Continuous Logistic Growth", fontsize=14, pad=15)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.legend(frameon=True, facecolor="white", edgecolor="none")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()

# Plot 2: Absolute Error/Difference Curve
plt.figure(figsize=(10, 4))
plt.plot(discrete_time, abs_diff, "s-", markersize=4, color="purple")

plt.title("Absolute Difference Between Logistic Models", fontsize=14, pad=15)
plt.xlabel("Time Step", fontsize=12)
plt.ylabel("Absolute Difference", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()
