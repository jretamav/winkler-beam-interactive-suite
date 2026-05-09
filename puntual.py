import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

# --- Funciones de Cálculo ---
def calcular_viga_analitica(EI, k, P):
    beta = (k / (4 * EI))**(1/4)
    x_vec = np.linspace(-10, 10, 1000)
    
    def evaluate_point(x_in):
        ax = np.abs(x_in)
        sgn = np.where(np.asarray(x_in) >= 0, 1.0, -1.0)
        y = -(P * beta / (2 * k)) * np.exp(-beta * ax) * (np.cos(beta * ax) + np.sin(beta * ax))
        M = (P / (4 * beta)) * np.exp(-beta * ax) * (np.cos(beta * ax) - np.sin(beta * ax))
        V = -sgn * (P / 2) * np.exp(-beta * ax) * np.cos(beta * ax)
        return y, M, V

    y_v, M_v, V_v = evaluate_point(x_vec)
    return x_vec, y_v, M_v, V_v, evaluate_point

# --- Variables Globales ---
EI, k, P, x_inspec = 250.0, 1000.0, 1000.0, 0.0

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(13, 10), sharex=True)
plt.subplots_adjust(top=0.90, bottom=0.22, left=0.12, right=0.75, hspace=0.35)
fig.suptitle('INFINITE BEAM WITH A POINT LOAD $P$ AT $x=0$', fontsize=14, fontweight='bold', color='navy')

x_v, y_v, M_v, V_v, eval_func = calcular_viga_analitica(EI, k, P)

l1, = ax1.plot(x_v, y_v, color='blue', lw=2)
l2, = ax2.plot(x_v, M_v, color='red', lw=2)
l3, = ax3.plot(x_v, V_v, color='green', lw=2)

p1, = ax1.plot(x_inspec, eval_func(x_inspec)[0], 'ko', zorder=5)
p2, = ax2.plot(x_inspec, eval_func(x_inspec)[1], 'ko', zorder=5)
p3, = ax3.plot(x_inspec, eval_func(x_inspec)[2], 'ko', zorder=5)

# --- Cuadros de Resultados Laterales ---
res_box1 = fig.text(0.78, 0.75, '', fontsize=11, fontweight='normal', color='blue',
                    bbox=dict(facecolor='aliceblue', edgecolor='blue', boxstyle='round,pad=0.5'))
res_box2 = fig.text(0.78, 0.48, '', fontsize=11, fontweight='normal', color='red',
                    bbox=dict(facecolor='snow', edgecolor='red', boxstyle='round,pad=0.5'))
res_box3 = fig.text(0.78, 0.22, '', fontsize=11, fontweight='normal', color='darkgreen',
                    bbox=dict(facecolor='honeydew', edgecolor='darkgreen', boxstyle='round,pad=0.5'))

for ax, lab in zip([ax1, ax2, ax3], ['$y(x)$ [m]', '$M(x)$ [kN·m]', '$V(x)$ [kN]']):
    ax.set_ylabel(lab)
    ax.axhline(0, color='black', lw=1.2)
    ax.grid(True, linestyle=':', alpha=0.6)
ax3.set_xlabel('Position along the beam $x$ [m]')

# --- Controles ---
s_ei = Slider(plt.axes([0.15, 0.12, 0.25, 0.02]), '$EI$: ', 100, 5000, valinit=EI)
s_k  = Slider(plt.axes([0.15, 0.08, 0.25, 0.02]), '$k$: ', 100, 5000, valinit=k)
s_p  = Slider(plt.axes([0.15, 0.04, 0.25, 0.02]), '$P$: ', 1, 5000, valinit=P)

t_ei = TextBox(plt.axes([0.48, 0.12, 0.07, 0.025]), 'Set $EI$: ', initial=str(EI))
t_k  = TextBox(plt.axes([0.48, 0.08, 0.07, 0.025]), 'Set $k$: ', initial=str(k))
t_p  = TextBox(plt.axes([0.48, 0.04, 0.07, 0.025]), 'Set $P$: ', initial=str(P))

# UNIDADES EN LETRA NORMAL (USANDO \text{})
fig.text(0.555, 0.12, r'[$\text{kN} \cdot \text{m}^2$]', fontsize=9, verticalalignment='center')
fig.text(0.555, 0.08, r'[$\text{kN}/\text{m}^2$]', fontsize=9, verticalalignment='center')
fig.text(0.555, 0.04, r'[$\text{kN}$]', fontsize=9, verticalalignment='center')

t_xi = TextBox(plt.axes([0.78, 0.08, 0.08, 0.035], facecolor='lightyellow'), 'Inspect $x$: ', initial="0.0")
fig.text(0.865, 0.08, r'[$\text{m}$]', fontsize=9, verticalalignment='center')

def redibujar(event_val=None):
    global EI, k, P, x_inspec, eval_func
    try:
        EI = float(t_ei.text); k = float(t_k.text); P = float(t_p.text); x_inspec = float(t_xi.text)
    except ValueError: return 

    x_v, y_new, M_new, V_new, eval_func = calcular_viga_analitica(EI, k, P)
    yi, mi, vi = eval_func(x_inspec)

    l1.set_ydata(new_y := y_new); l2.set_ydata(new_M := M_new); l3.set_ydata(new_V := V_new)
    p1.set_data([x_inspec], [yi]); p2.set_data([x_inspec], [mi]); p3.set_data([x_inspec], [vi])
    
    # RESULTADOS CON UNIDADES EN LETRA NORMAL
    res_box1.set_text(f"At $x = {x_inspec}$ m\n$y = {yi:.5f}$ [m]")
    res_box2.set_text(f"At $x = {x_inspec}$ m\n$M = {mi:.3f}$ [kN·m]")
    res_box3.set_text(f"At $x = {x_inspec}$ m\n$V = {vi:.3f}$ [kN]")

    for ax, data in zip([ax1, ax2, ax3], [new_y, new_M, new_V]):
        range_d = max(data) - min(data)
        ax.set_ylim(min(data) - 0.2*range_d - 0.01, max(data) + 0.2*range_d + 0.01)
    
    s_ei.eventson = s_k.eventson = s_p.eventson = False
    s_ei.set_val(EI); s_k.set_val(k); s_p.set_val(P)
    s_ei.eventson = s_k.eventson = s_p.eventson = True
    fig.canvas.draw_idle()

def slider_update(val):
    t_ei.set_val(f"{s_ei.val:.1f}"); t_k.set_val(f"{s_k.val:.1f}"); t_p.set_val(f"{s_p.val:.1f}")
    redibujar()

s_ei.on_changed(slider_update); s_k.on_changed(slider_update); s_p.on_changed(slider_update)
t_ei.on_submit(redibujar); t_k.on_submit(redibujar); t_p.on_submit(redibujar); t_xi.on_submit(redibujar)

redibujar()
plt.show()
