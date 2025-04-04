import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox


# Custom symbols for stability indicators
def get_symbol(stable):
    return "\u2714" if stable else "\u274C"


# Create figure and layout
fig = plt.figure(figsize=(10, 6))

# PARAMETERS
ax_parameters = plt.axes([0.05, 0.1, 0.2, 0.75])
ax_parameters.set_frame_on(False)
ax_parameters.axes.get_xaxis().set_visible(False)
ax_parameters.axes.get_yaxis().set_visible(False)

# Crystal
ax_parameters.text(0.5, 0.95, "Crystal", fontsize=12, fontweight='bold', ha='center', color='red')
# Sliders for l and lambda
ax_l = plt.axes([0.07, 0.75, 0.15, 0.03])
l_slider = Slider(ax_l, '$l$', 0.1, 2.0, valinit=1.0)

ax_lambda = plt.axes([0.07, 0.70, 0.15, 0.03])
lambda_slider = Slider(ax_lambda, '$\lambda$ (nm)', 300, 1800, valinit=780)

# Entry boxes for n and Lambda
ax_n = plt.axes([0.04, 0.62, 0.07, 0.05])
n_box = TextBox(ax_n, '$n$:')

ax_lambda_p = plt.axes([0.17, 0.62, 0.07, 0.05])
lambda_p_box = TextBox(ax_lambda_p, '$\Lambda$ ($\mu$m):')

# Entry box for omega_opt
ax_wopt = plt.axes([0.04, 0.55, 0.07, 0.05])
wopt_box = TextBox(ax_wopt, '$\omega_{opt}$:')

# Cavity
# Sliders for R, L, and d_c
ax_parameters.text(0.5, 0.55, "Cavity", fontsize=12, fontweight='bold', ha='center', color='red')

ax_R = plt.axes([0.07, 0.45, 0.15, 0.03])
R_slider = Slider(ax_R, '$R$ (mm)', 10, 200, valinit=50)

ax_L = plt.axes([0.07, 0.40, 0.15, 0.03])
L_slider = Slider(ax_L, '$L$ (mm)', 50, 200, valinit=100)

ax_dc = plt.axes([0.07, 0.35, 0.15, 0.03])
dc_slider = Slider(ax_dc, '$d_c$ (mm)', 10, 50, valinit=15)

# Conditions
ax_parameters.text(0.5, 0.25, "Conditions", fontsize=12, fontweight='bold', ha='center', color='red')

# ax_stability = plt.axes([0.07, 0.22, 0.15, 0.03])
stability_text = ax_parameters.text(0.07, 0.15, "Stability: ✕", fontsize=10, ha='black', color='red')
# TODO When stability is okay, change it to ✓ and the color to green, maybe two text box so the full label isn't red or green

# ax_folding_angle = plt.axes([0.07, 0.18, 0.15, 0.03])
folding_angle_text = ax_parameters.text(0.07, 0.1, "Folding Angle: 0°", fontsize=10, ha='left', color='black')

# ax_w1_param = plt.axes([0.07, 0.14, 0.15, 0.03])
w1_text = ax_parameters.text(0.07, 0.05, "w₁: -", fontsize=10, ha='left', color='black')

# ax_w2_param = plt.axes([0.07, 0.10, 0.15, 0.03])
w2_text = ax_parameters.text(0.5, 0.05, "w₂: -", fontsize=10, ha='left', color='black')


# WIDTH
ax_w1 = plt.axes([0.3, 0.5, 0.3, 0.35])
ax_w2 = plt.axes([0.65, 0.5, 0.3, 0.35])

# SCHEMA OF THE CAVITY
ax_cavity_diagram = plt.axes([0.3, 0.1, 0.65, 0.35])
ax_cavity_diagram.axes.get_xaxis().set_visible(False)
ax_cavity_diagram.axes.get_yaxis().set_visible(False)
ax_cavity_diagram.set_frame_on(False)

plt.show()
