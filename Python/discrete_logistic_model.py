import matplotlib.pyplot as plt
import numpy as np


def discrete_logistic_growth(p0, r, K, t_max):
    population = np.zeros(t_max + 1)
    population[0] = p0
    for t in range(t_max):
        p_current = population[t]
        p_next = p_current + r * p_current * (1 - p_current / K)
        population[t + 1] = max(0, p_next)
    return population


# --- Parameters ---
p0 = 10  # Initial population
K = 500  # Carrying capacity
t_max = 50  # Time steps

# --- Values of 'r' to observe different dynamics ---
r_values = {
    "Smooth Stabilization (r=0.7)": 0.7,
    "Stable Oscillations (r=1.9)": 1.9,
    "Pure Chaos (r=2.6)": 2.6,
}

# --- Create Plot Layout ---
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharex="col", sharey="col")
plt.subplots_adjust(hspace=0.3, wspace=0.25)

time_steps = np.arange(t_max + 1)
p_vals = np.linspace(0, K * 1.5, 400)


def update_func(p, r, K):
    return p + r * p * (1 - p / K)


# --- Plotting Loop ---
for idx, (title, r) in enumerate(r_values.items()):
    pop_sizes = discrete_logistic_growth(p0, r, K, t_max)
    ax_time, ax_cobweb = axes[idx, 0], axes[idx, 1]

    # 1. Left Subplot: Time-Series Line Chart
    ax_time.plot(
        time_steps,
        pop_sizes,
        color="royalblue",
        marker="o",
        markersize=3,
        linestyle="-",
        linewidth=1.2,
    )
    ax_time.axhline(K, color="crimson", linestyle="--", alpha=0.7)
    ax_time.set_title(title, fontsize=11, fontweight="bold", loc="left")
    ax_time.set_ylabel("Population ($P_t$)", fontsize=10)
    ax_time.grid(True, linestyle=":", alpha=0.6)

    if idx == 0:
        ax_time.text(
            t_max * 0.6,
            K * 1.05,
            f"Carrying Capacity (K={K})",
            color="crimson",
            fontsize=9,
        )

    # 2. Right Subplot: Cobweb Diagram
    ax_cobweb.plot(p_vals, update_func(p_vals, r, K), "g-", label="$P_{t+1}=f(P_t)$")
    ax_cobweb.plot(p_vals, p_vals, "k--", alpha=0.5, label="$P_{t+1}=P_t$")

    # Generate Cobweb tracing coordinates
    cx, cy = [], []
    for i in range(len(pop_sizes) - 1):
        cx.extend([pop_sizes[i], pop_sizes[i]])
        cy.extend([pop_sizes[i], pop_sizes[i + 1]])
        cx.extend([pop_sizes[i], pop_sizes[i + 1]])
        cy.extend([pop_sizes[i + 1], pop_sizes[i + 1]])

    ax_cobweb.plot(cx, cy, "r-", linewidth=0.8, alpha=0.6)
    ax_cobweb.set_title(f"Cobweb Attractor (r={r})", fontsize=11, loc="left")
    ax_cobweb.set_ylabel("$P_{t+1}$", fontsize=10)
    ax_cobweb.grid(True, linestyle=":", alpha=0.6)

# Set global axis labels for the outer edge plots
for ax in axes[-1, :]:
    ax.set_xlabel("Time Steps (t)" if ax == axes[-1, 0] else "Current $P_t$")

axes[0, 1].set_xlim(0, K * 1.5)
axes[0, 1].set_ylim(0, K * 1.5)

plt.suptitle(
    "Discrete Logistic Growth: Time-Series vs. Cobweb Attractors",
    fontsize=14,
    fontweight="bold",
    y=0.96,
)
plt.show()
