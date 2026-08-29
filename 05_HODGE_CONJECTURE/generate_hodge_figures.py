import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs(r"C:\Users\papic\Desktop\MILLENNIUM_PRIZE_SERIES\05_HODGE_CONJECTURE", exist_ok=True)
out_dir = r"C:\Users\papic\Desktop\MILLENNIUM_PRIZE_SERIES\05_HODGE_CONJECTURE"

plt.style.use('dark_background')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9

# FIGURE 1: Hodge Diamond Decomposition
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)

# Hodge Diamond points for 3-fold
points = {
    (0, 3): "h^{0,0} = 1",
    (-1, 2): "h^{1,0} = 0", (1, 2): "h^{0,1} = 0",
    (-2, 1): "h^{2,0} = 0", (0, 1): "h^{1,1} = 19", (2, 1): "h^{0,2} = 0",
    (-3, 0): "h^{3,0} = 1", (-1, 0): "h^{2,1} = 19", (1, 0): "h^{1,2} = 19", (3, 0): "h^{0,3} = 1",
    (-2, -1): "h^{3,1} = 0", (0, -1): "h^{2,2} = 19", (2, -1): "h^{1,3} = 0",
    (-1, -2): "h^{3,2} = 0", (1, -2): "h^{2,3} = 0",
    (0, -3): "h^{3,3} = 1"
}

for (x, y), label in points.items():
    is_hodge_class = "(k, k)" in label or "h^{1,1}" in label or "h^{2,2}" in label or "h^{0,0}" in label or "h^{3,3}" in label
    color = '#10b981' if is_hodge_class else '#38bdf8'
    ax.plot(x, y, 'o', color=color, markersize=10)
    ax.text(x, y + 0.28, label, color=color, fontweight='bold', fontsize=8, ha='center')

# Highlight Hodge central axis
ax.axvline(0, color='#f59e0b', linestyle='--', alpha=0.5, label=r'Hodge $(k, k)$ Rational Central Line')

ax.set_xlim(-4, 4)
ax.set_ylim(-3.8, 3.8)
ax.axis('off')
ax.set_title(r"$\mathbf{\text{Hodge Diamond } h^{p, q} \text{ and Rational Cycle Realization on Complex 3-Fold}}$", fontsize=11, color='#f1f5f9', pad=10)
ax.legend(loc='upper right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig1_hodge_diamond_decomposition.png"))
plt.close()

# FIGURE 2: Algebraic Cycles on Projective Variety X
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))

theta = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(theta), np.sin(theta), color='#06b6d4', linewidth=2.5, label=r'Projective Manifold $X \subset \mathbb{P}^N(\mathbb{C})$')
ax.plot(0.7*np.cos(theta), 0.3*np.sin(theta) + 0.2, color='#f43f5e', linewidth=2, label=r'Algebraic Cycle $Z_1$ (Codim k)')
ax.plot(0.4*np.cos(theta) - 0.3, 0.8*np.sin(theta) - 0.1, color='#a855f7', linewidth=2, label=r'Algebraic Cycle $Z_2$ (Codim k)')

ax.set_title(r"$\mathbf{\text{Poincare Duality: Rational Class } \alpha = \sum c_i [Z_i] \in \mathrm{Hdg}^{2k}(X, \mathbb{Q})}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_aspect('equal')
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='upper right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig2_algebraic_cycles_chow_variety.png"))
plt.close()

# FIGURE 3: Harmonic Forms & Lelong Numbers
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
r = np.linspace(0.01, 2, 200)
# Current density and Lelong number
lelong_density = 1.0 + 0.5 * np.exp(-3*r)

ax.plot(r, lelong_density, color='#10b981', linewidth=2.2, label=r'Positive Closed Current Density $\Theta_T(r)$')
ax.axhline(1.0, color='#f59e0b', linestyle='--', linewidth=1.5, label=r'Lelong Number $\nu(T, x) = \lim_{r \to 0} \Theta_T(r) \in \mathbb{Q}$')

ax.set_title(r"$\mathbf{\text{Lelong Regularization of Positive Closed }(k, k)\text{-Currents into Algebraic Cycles}}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_xlabel("Ball Radius r around Singularity", color='#94a3b8')
ax.set_ylabel(r"Area Ratio $\nu(T, x, r)$", color='#94a3b8')
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='upper right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig3_harmonic_forms_lelong_currents.png"))
plt.close()

# FIGURE 4: Hard Lefschetz Isomorphism
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
k_degs = np.arange(0, 7)
dim_hk = np.array([1, 2, 8, 22, 8, 2, 1])

ax.bar(k_degs, dim_hk, color='#38bdf8', edgecolor='#ec4899', width=0.55, alpha=0.85, label=r'Cohomology Dimension $\dim H^k(X, \mathbb{C})$')
ax.plot(k_degs, dim_hk, color='#ec4899', marker='o', linewidth=1.8, label=r'Hard Lefschetz Reflection: $L^{n-k}: H^k \cong H^{2n-k}$')

ax.set_title(r"$\mathbf{\text{Hard Lefschetz Isomorphism and Primitive Decomposition of Hodge Classes}}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_xlabel("Cohomology Degree k", color='#94a3b8')
ax.set_ylabel(r"Betti Number $b_k$", color='#94a3b8')
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='upper left', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig4_hard_lefschetz_isomorphism.png"))
plt.close()

print("ALL HODGE CONJECTURE FIGURES GENERATED SUCCESSFULLY!")
