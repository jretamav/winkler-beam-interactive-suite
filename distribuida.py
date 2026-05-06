import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

# --- Funciones de Cálculo para Carga Distribuida ---
def calcular_viga_analitica(EI, k, q, a):
    beta = (k / (4 * EI))**(1/4)
    x_vec = np.linspace(-10, 10, 1000)
    
    # Funciones auxiliares de Winkler
    def D(z): return np.exp(-z) * np.cos(z)
    def B(z): return np.exp(-z) * np.sin(z)
    def C(z): return np.exp(-z) * (np.cos(z) - np.sin(z))

    def obtener_punto(x_in):
        ax = np.abs(x_in)
        sgn = np.sign(x_in) if x_in != 0 else 1.0
        
        if ax <= a / 2:
            # Zona interior (|x| <= a/2)
            # Deflexión y(x): y positivo hacia arriba -> y negativo hacia abajo
            y = -(q / (2 * k)) * (2 - D(beta * (a / 2 + ax)) - D(beta * (a / 2 - ax)))
            # Momento M(x):
            M = (q / (4 * beta**2)) * (B(beta * (a / 2 + ax)) + B(beta * (a / 2 - ax)))
            # Cortante V(x) = dM/dx (CORREGIDO PARA GARANTIZAR CONTINUIDAD)
            V_mag = (q / (4 * beta)) * (C(beta * (a / 2 + ax)) - C(beta * (a / 2 - ax)))
            V = sgn * V_mag
        else:
            # Zona exterior (|x| > a/2)
            y = -(q / (2 * k)) * (D(beta * (ax - a / 2)) - D(beta * (ax + a / 2)))
            M = -(q / (4 * beta**2)) * (B(beta * (ax - a / 2)) - B(beta * (ax + a / 2)))
            V_mag = -(q / (4 * beta)) * (C(beta * (ax - a / 2)) - C(beta * (ax + a / 2)))
            V = sgn * V_mag
            
        return y, M, V

    res = [obtener_punto(val) for val in x_vec]
    y_v = np.array([r[0] for r in res])
    M_v = np.array([r[1] for r in res])
    V_v = np.array([r[2] for r in res])
    
    return x_vec, y_v, M_v, V_v, obtener_punto

# --- Variables Globales ---
EI, k, q, a_len, x_inspec = 250.0, 1000.0, 500.0, 2.0, 0.0

# --- Configuración de la Figura ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(13, 10), sharex=True)
plt.subplots_adjust(top=0.90, bottom=0.22, left=0.12, right=0.75, hspace=0.35)
fig.suptitle(r'INFINITE BEAM WITH A DISTRIBUTED LOAD $q$ OVER LENGTH $a$', fontsize=14, fontweight='bold', color='navy')

x_v, y_v, M_v, V_v, eval_func = calcular_viga_analitica(EI, k, q, a_len)

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
s_ei = Slider(plt.axes([0.15, 0.14, 0.20, 0.015]), '$EI$: ', 100, 5000, valinit=EI)
s_k  = Slider(plt.axes([0.15, 0.10, 0.20, 0.015]), '$k$: ', 100, 5000, valinit=k)
s_q  = Slider(plt.axes([0.15, 0.06, 0.20, 0.015]), '$q$: ', 1, 5000, valinit=q)
s_a  = Slider(plt.axes([0.15, 0.02, 0.20, 0.015]), '$a$: ', 0.1, 10, valinit=a_len)

t_ei = TextBox(plt.axes([0.43, 0.14, 0.06, 0.02]), 'Set $EI$: ', initial=str(EI))
t_k  = TextBox(plt.axes([0.43, 0.10, 0.06, 0.02]), 'Set $k$: ', initial=str(k))
t_q  = TextBox(plt.axes([0.43, 0.06, 0.06, 0.02]), 'Set $q$: ', initial=str(q))
t_a  = TextBox(plt.axes([0.43, 0.02, 0.06, 0.02]), 'Set $a$: ', initial=str(a_len))

# UNIDADES EN LETRA NORMAL
fig.text(0.50, 0.14, r'[$\text{kN} \cdot \text{m}^2$]', fontsize=8, verticalalignment='center')
fig.text(0.50, 0.10, r'[$\text{kN}/\text{m}^2$]', fontsize=8, verticalalignment='center')
fig.text(0.50, 0.06, r'[$\text{kN}/\text{m}$]', fontsize=8, verticalalignment='center')
fig.text(0.50, 0.02, r'[$\text{m}$]', fontsize=8, verticalalignment='center')

t_xi = TextBox(plt.axes([0.78, 0.08, 0.08, 0.035], facecolor='lightyellow'), 'Inspect $x$: ', initial="0.0")
fig.text(0.865, 0.08, r'[$\text{m}$]', fontsize=9, verticalalignment='center')

def redibujar(event_val=None):
    global EI, k, q, a_len, x_inspec, eval_func
    try:
        EI = float(t_ei.text); k = float(t_k.text); q = float(t_q.text)
        a_len = float(t_a.text); x_inspec = float(t_xi.text)
    except ValueError: return 

    x_v, y_new, M_new, V_new, eval_func = calcular_viga_analitica(EI, k, q, a_len)
    yi, mi, vi = eval_func(x_inspec)

    l1.set_ydata(new_y := y_new); l2.set_ydata(new_M := M_new); l3.set_ydata(new_V := V_new)
    p1.set_data([x_inspec], [yi]); p2.set_data([x_inspec], [mi]); p3.set_data([x_inspec], [vi])
    
    res_box1.set_text(f"At $x = {x_inspec}$ m\n$y = {yi:.5f}$ [m]")
    res_box2.set_text(f"At $x = {x_inspec}$ m\n$M = {mi:.3f}$ [kN·m]")
    res_box3.set_text(f"At $x = {x_inspec}$ m\n$V = {vi:.3f}$ [kN]")

    for ax, data in zip([ax1, ax2, ax3], [new_y, new_M, new_V]):
        range_d = max(data) - min(data)
        if range_d < 1e-6: range_d = 0.1
        ax.set_ylim(min(data) - 0.2*range_d - 0.01, max(data) + 0.2*range_d + 0.01)
    
    s_ei.eventson = s_k.eventson = s_q.eventson = s_a.eventson = False
    s_ei.set_val(EI); s_k.set_val(k); s_q.set_val(q); s_a.set_val(a_len)
    s_ei.eventson = s_k.eventson = s_q.eventson = s_a.eventson = True
    fig.canvas.draw_idle()

def slider_update(val):
    t_ei.set_val(f"{s_ei.val:.1f}"); t_k.set_val(f"{s_k.val:.1f}")
    t_q.set_val(f"{s_q.val:.1f}"); t_a.set_val(f"{s_a.val:.1f}")
    redibujar()

s_ei.on_changed(slider_update); s_k.on_changed(slider_update)
s_q.on_changed(slider_update); s_a.on_changed(slider_update)
t_ei.on_submit(redibujar); t_k.on_submit(redibujar)
t_q.on_submit(redibujar); t_a.on_submit(redibujar); t_xi.on_submit(redibujar)

redibujar()
plt.show()
