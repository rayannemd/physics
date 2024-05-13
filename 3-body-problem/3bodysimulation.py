import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# momento angular 0
m3 = 1  # pode variar
v1 = 0.39295
v2 = 0.09758

# constantes
m1 = 1
m2 = 1
m3 = m3
x1_0 = -0.5
y1_0 = 0
x2_0 = 0.5
y2_0 = 0
x3_0 = 0
y3_0 = 0

# condicoes iniciais
vx1_0 = v1
vy1_0 = v2
vx2_0 = v1
vy2_0 = v2
vx3_0 = -2 * v1 / m3
vy3_0 = -2 * v2 / m3

# equacao diferencial
def dSdt(t, S):
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3 = S
    r12 = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    r13 = np.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    r23 = np.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    return [
        vx1,
        vy1,
        vx2,
        vy2,
        vx3,
        vy3,
        m2 / r12**3 * (x2 - x1) + m3 / r13**3 * (x3 - x1),  # massa 1
        m2 / r12**3 * (y2 - y1) + m3 / r13**3 * (y3 - y1),
        m1 / r12**3 * (x1 - x2) + m3 / r23**3 * (x3 - x2),  # massa 2
        m1 / r12**3 * (y1 - y2) + m3 / r23**3 * (y3 - y2),
        m1 / r13**3 * (x1 - x3) + m2 / r23**3 * (x2 - x3),  # massa 3
        m1 / r13**3 * (y1 - y3) + m2 / r23**3 * (y2 - y3),
    ]

t = np.linspace(0, 20, 1000)

# metodo DOP853 para resolver EDOs
sol = solve_ivp(
    dSdt,
    (0, 20),
    y0=[x1_0, y1_0, x2_0, y2_0, x3_0, y3_0, vx1_0, vy1_0, vx2_0, vy2_0, vx3_0, vy3_0],
    method="DOP853",
    t_eval=t,
    rtol=1e-10,
    atol=1e-13,
)

# separando as solucoes
t = sol.t
x1 = sol.y[0]
y1 = sol.y[1]
x2 = sol.y[2]
y2 = sol.y[3]
x3 = sol.y[4]
y3 = sol.y[5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.grid()

(ln1,) = ax.plot([], [], [], "ro", markersize=6)

def animate(i):
    ln1.set_data([x1[i], x2[i], x3[i]], [y1[i], y2[i], y3[i]])
    ln1.set_3d_properties([0, 0, 0])
    ax.set_title("Time = {:.1f} Years".format(t[i]))
    return (ln1,)

# limites do grafico
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=50, blit=True)
ani.save("3bodies.gif", writer="pillow", fps=30)