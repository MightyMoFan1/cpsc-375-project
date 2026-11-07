import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp

def logistic_growth(P0, t, r, K):
    dydt = r * P0 * (1 - P0 / K)
    return dydt

def simulate_logistic_growth(P0, r, K, t):
    y = solve_ivp(logistic_growth, [t[0], t[-1]], [P0], t_eval=t, args=(r, K))
    return y.y[0]

# Parameters
t = np.linspace(0, 10, 100)  # Time points
P0 = 1  # Initial population
sol = simulate_logistic_growth(P0, r=0.5, K=10, t=t)

plt.plot(t, sol, color='blue', label='Population')
plt.title('(Observed) Logistic Growth Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.axhline(y=10, color='red', linestyle='--', label='Carrying Capacity (K)')
plt.show()



