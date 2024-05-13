import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# condicoes iniciais
m1 = 1  # terra
m2 = 333000  # sol
x1_0 = 0.5
y1_0 = 0
x2_0 = 0
y2_0 = 0
vx1_0 = 0
vy1_0 = np.sqrt(m2)
vx2_0 = 0
vy2_0 = 0

# equacao diferencial
def dSdt(S, t):
    x1, y1, x2, y2, vx1, vy1, vx2, vy2 = S
    r12 = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return [
        vx1,
        vy1,
        vx2,
        vy2,
        m2 / r12**3 * (x2 - x1),
        m2 / r12**3 * (y2 - y1),
        m1 / r12**3 * (x1 - x2),
        m1 / r12**3 * (y1 - y2),
    ]

t = np.linspace(0, 1, 10000)

sol = odeint(dSdt, y0=[x1_0, y1_0, x2_0, y2_0, vx1_0, vy1_0, vx2_0, vy2_0], t=t)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.grid()

# separando as solucoes
x1 = sol[:, 0]
y1 = sol[:, 1]
x2 = sol[:, 2]
y2 = sol[:, 3]

(ln1,) = ax.plot([], [], [], "ro--", lw=3, markersize=8)

def animate(i):
    ln1.set_data([x1[i], x2[i]], [y1[i], y2[i]])
    ln1.set_3d_properties([0, 0])
    ax.set_title("Time = {:.2f} Years".format(t[i]))
    return (ln1,)

# limites do grafico
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

ani = animation.FuncAnimation(fig, animate, frames=len(t) // 10, interval=50, blit=True)
ani.save("2bodies.gif", writer="pillow", fps=30)
