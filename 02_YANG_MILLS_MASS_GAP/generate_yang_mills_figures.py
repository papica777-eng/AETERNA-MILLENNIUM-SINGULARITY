import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs(r"C:\Users\papic\Desktop\MILLENNIUM_PRIZE_SERIES\02_YANG_MILLS_MASS_GAP", exist_ok=True)
out_dir = r"C:\Users\papic\Desktop\MILLENNIUM_PRIZE_SERIES\02_YANG_MILLS_MASS_GAP"

plt.style.use('dark_background')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9

# FIGURE 1: Gauge Orbit Space A/G and Gribov Horizon
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
theta = np.linspace(0, 2*np.pi, 300)
r_gribov = 2.5 + 0.3*np.sin(3*theta)
x_g = r_gribov * np.cos(theta)
y_g = r_gribov * np.sin(theta)

ax.fill(x_g, y_g, color='#0284c7', alpha=0.25, label=r'Fundamental Modular Domain $\Omega \subset \mathcal{A}/\mathcal{G}$')
ax.plot(x_g, y_g, color='#38bdf8', linewidth=2.2, label=r'First Gribov Horizon $\partial \Omega$ ($\det(\mathcal{M}) = 0$)')

# Vacuum state at origin
ax.plot(0, 0, 'o', color='#f59e0b', markersize=9, label=r'Unique Gauge-Invariant Vacuum $|\Omega\rangle$')
ax.text(0.15, -0.2, r'$|\Omega\rangle$', color='#f59e0b', fontweight='bold', fontsize=11)

# Gauge Orbit fibers
for rad in [0.8, 1.5, 2.0]:
    x_c = rad * np.cos(theta)
    y_c = rad * np.sin(theta)
    ax.plot(x_c, y_c, ':', color='#94a3b8', alpha=0.4)

ax.set_title(r"$\mathbf{\text{Geometry of Non-Abelian Orbit Space } \mathcal{A}/\mathcal{G} \text{ and Gribov Horizon}}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_xlabel(r"Gauge Field Mode $A_\mu^{(1)}$", color='#94a3b8')
ax.set_ylabel(r"Gauge Field Mode $A_\mu^{(2)}$", color='#94a3b8')
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='upper right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig1_gauge_orbit_gribov_horizon.png"))
plt.close()

# FIGURE 2: Energy Spectrum and Mass Gap Delta > 0
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
energies = np.linspace(0, 5, 500)

# Density of states rho(E)
delta = 1.45 # Mass gap in GeV
rho = np.zeros_like(energies)
rho[energies >= delta] = 1.8 * np.sqrt(energies[energies >= delta] - delta) * np.exp(-0.2*(energies[energies >= delta] - delta))

ax.plot(energies, rho, color='#10b981', linewidth=2.2, label=r'Continuum Massive Spectrum $\mathrm{Spec}(\hat{H}_{YM}) \geq \Delta$')
ax.fill_between(energies, 0, rho, where=(energies >= delta), color='#10b981', alpha=0.25)

# Vacuum delta peak at E = 0
ax.vlines(0, 0, 2.5, color='#f59e0b', linewidth=3.5, label=r'Isolated Vacuum Energy $E_0 = 0$')
ax.plot(0, 2.5, 'o', color='#f59e0b', markersize=8)

# Shaded Gap Region
ax.axvspan(0.01, delta, color='#f43f5e', alpha=0.18, label=f'Strict Mass Gap $\\Delta = {delta}$ GeV > 0 (No States)')
ax.axvline(delta, color='#f43f5e', linestyle='--', linewidth=1.8)

ax.text(0.4, 1.2, r'$\mathbf{MASS\ GAP\ \Delta > 0}$', color='#f43f5e', fontweight='bold', fontsize=11)
ax.text(delta + 0.1, 0.5, r'Lowest Glueball State $0^{++}$', color='#10b981', fontsize=9)

ax.set_title(r"$\mathbf{\text{Energy Spectral Density } \rho(E) \text{ Exhibiting Strict Mass Gap } \Delta > 0}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_xlabel(r"Energy Eigenvalue $E$ (GeV)", color='#94a3b8')
ax.set_ylabel(r"Spectral Density $\rho(E) = \operatorname{Tr} \delta(E - \hat{H}_{YM})$", color='#94a3b8')
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='upper right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig2_mass_gap_spectral_density.png"))
plt.close()

# FIGURE 3: Wilson Loop Confinement Area Law
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
r_dist = np.linspace(0.1, 3.5, 300)
# Cornell static quark potential V(r) = -alpha/r + sigma * r
sigma_string = 0.85 # GeV/fm string tension
alpha_coulomb = 0.28
v_potential = -alpha_coulomb / r_dist + sigma_string * r_dist

ax.plot(r_dist, v_potential, color='#a855f7', linewidth=2.5, label=r'Static Confining Potential $V(r) = -\frac{\alpha}{r} + \sigma r$')
ax.plot(r_dist, sigma_string * r_dist, '--', color='#ec4899', alpha=0.7, label=f'Linear Confinement String Tension $\\sigma = {sigma_string}$ GeV/fm')

ax.set_title(r"$\mathbf{\text{Wilson Loop Area Law: Color Confinement with Non-Zero String Tension }\sigma > 0}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_xlabel(r"Quark-Antiquark Distance $r$ (fm)", color='#94a3b8')
ax.set_ylabel(r"Static Potential $V(r)$ (GeV)", color='#94a3b8')
ax.set_ylim(-1.5, 3.0)
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='lower right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig3_wilson_loop_confinement_area_law.png"))
plt.close()

# FIGURE 4: Instanton Tunneling Energy & Topological Sectors
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
q_coord = np.linspace(-2.5, 2.5, 400)
# Periodic instanton potential V(Q) = V_0 * sin^2(pi * Q)
v_instanton = 1.6 * (np.sin(np.pi * q_coord))**2

ax.plot(q_coord, v_instanton, color='#f59e0b', linewidth=2.2, label=r'Instanton Periodic Potential $V(Q) = V_0 \sin^2(\pi Q)$')
ax.fill_between(q_coord, 0, v_instanton, color='#f59e0b', alpha=0.15)

for q_val in [-2, -1, 0, 1, 2]:
    ax.plot(q_val, 0, 'o', color='#38bdf8', markersize=7)
    ax.text(q_val - 0.15, -0.22, f'Q = {q_val}', color='#38bdf8', fontweight='bold', fontsize=9)

ax.annotate('Topological Tunneling\n(Instanton Action S_0)', xy=(0.5, 1.6), xytext=(0.8, 1.85),
            arrowprops=dict(arrowstyle='->', color='#ec4899', lw=1.5),
            color='#ec4899', fontweight='bold', fontsize=9)

ax.set_title(r"$\mathbf{\text{Topological Vacua } |n\rangle \text{ and Non-Perturbative Mass Generation via Instantons}}$", fontsize=11, color='#f1f5f9', pad=10)
ax.set_xlabel(r"Chern-Simons Topological Coordinate $Q \in \pi_3(G) \cong \mathbb{Z}$", color='#94a3b8')
ax.set_ylabel(r"Effective Action Energy Barrier $V(Q)$", color='#94a3b8')
ax.set_ylim(-0.35, 2.2)
ax.grid(True, color='#1e293b', linestyle='--', alpha=0.5)
ax.legend(loc='upper right', framealpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig4_instanton_tunneling_energy.png"))
plt.close()

print("ALL YANG-MILLS FIGURES GENERATED SUCCESSFULLY!")
