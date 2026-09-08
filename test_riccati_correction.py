import numpy as np
from scipy.integrate import solve_ivp

class RiccatiNanogRegulator:
    def __init__(self, alpha=0.04, beta=1.5, gamma=0.6, delta=1.0, R_val=0.05):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.R_inv = 1.0 / R_val
        self.B = np.array([[1.0], [0.0]])
        self.Q = np.array([[1.0, 0.0], [0.0, 100.0]])

    def jacobian_along_instanton(self, O, N):
        def dHill(X):
            return 4.0 * (X**3) / ((1.0 + X**4)**2)
        dfO_dO = self.beta * dHill(O) - self.delta
        dfO_dN = self.gamma * dHill(N)
        dfN_dO = self.gamma * dHill(O)
        dfN_dN = self.beta * dHill(N) - self.delta
        return np.array([[dfO_dO, dfO_dN], [dfN_dO, dfN_dN]])

    def riccati_rhs_correct(self, t, P_flat, instanton_func):
        P = P_flat.reshape((2, 2))
        O, N = instanton_func(t)
        A = self.jacobian_along_instanton(O, N)
        BB_term = P @ self.B @ (self.B.T * self.R_inv) @ P
        # The Riccati ODE is -dP/dt = A^T P + P A - P B R^-1 B^T P + Q
        # Therefore: dP/dt = - (A^T P + P A - P B R^-1 B^T P + Q)
        dP_dt = -(A.T @ P + P @ A - BB_term + self.Q)
        return dP_dt.flatten()

regulator = RiccatiNanogRegulator(R_val=0.05)

def instanton_path(t):
    O_t = 0.2454 + (0.9992 - 0.2454) * (t / 0.50)**2
    N_t = 0.0422 + (0.3662 - 0.0422) * (t / 0.50)**4
    return O_t, N_t

P_terminal = np.array([[10.0, 0.0], [0.0, 500.0]]).flatten()

sol = solve_ivp(
    fun=lambda t, y: regulator.riccati_rhs_correct(t, y, instanton_path),
    t_span=(0.50, 0.0),
    y0=P_terminal,
    t_eval=np.linspace(0.50, 0.0, 6),
    method='RK45'
)

print(f"Status: {sol.status}, Success: {sol.success}")
print(f"{'Time (t)':<10}{'P_11 (Oct4)':<18}{'P_22 (Nanog)':<18}{'Feedback Gain K1':<18}")
print("-" * 65)
for i in range(len(sol.t)):
    P_mat = sol.y[:, i].reshape((2, 2))
    K = regulator.R_inv * (regulator.B.T @ P_mat)
    print(f"{sol.t[i]:<10.2f}{P_mat[0,0]:<18.4f}{P_mat[1,1]:<18.4f}{K[0,0]:<18.4f}")
