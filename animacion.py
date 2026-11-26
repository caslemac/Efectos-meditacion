
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from pathlib import Path

# Importar nuestro modelo de Kuramoto
from graficar_kuramoto import simular, N, T, pasos, tiempos

# Ejecutar la simulación
K = 0.5
fases, r = simular(K)

# Crear dos gráficas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfica izquierda: osciladores
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_aspect("equal")
ax1.set_title("Fases de los osciladores")

# Dibujar circunferencia
angulo = np.linspace(0, 2*np.pi, 200)
ax1.plot(np.cos(angulo), np.sin(angulo), color="gray")

# Crear puntos
puntos, = ax1.plot([], [], "o", markersize=9)

# Gráfica derecha: sincronización
ax2.set_xlim(0, T)
ax2.set_ylim(0, 1.05)
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("Sincronización r(t)")
ax2.set_title("Evolución de la sincronización")
ax2.grid(alpha=0.3)

linea, = ax2.plot([], [], color="blue")

# Texto para mostrar tiempo y sincronización
texto = ax2.text(0.05, 0.9, "", transform=ax2.transAxes)


# Actualizar los fotogramas
def actualizar(frame):
    theta = fases[frame]

    x = np.cos(theta)
    y = np.sin(theta)

    puntos.set_data(x, y)
    linea.set_data(tiempos[:frame+1], r[:frame+1])

    texto.set_text(
        f"t = {tiempos[frame]:.2f} s\n"
        f"r = {r[frame]:.3f}"
    )

    return puntos, linea, texto


# Crear la animación
animacion = FuncAnimation(
    fig,
    actualizar,
    frames=range(0, pasos + 1, 20),
    interval=50,
    blit=True
)

plt.tight_layout()

# Guardar animación
salida = Path(__file__).resolve().parent / "resultados" / "animaciones"
salida.mkdir(parents=True, exist_ok=True)

animacion.save(
    salida / "kuramoto.gif",
    writer=PillowWriter(fps=20)
)

print("Animación guardada en:", salida / "kuramoto.gif")

# Mostrar animación
plt.show()

