
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. MODELO DE KURAMOTO
# ==========================================

def kuramoto(theta, omega, K):
    # Forma equivalente del acoplamiento global
    z = np.mean(np.exp(1j * theta))

    return omega + K * np.imag(z * np.exp(-1j * theta))


# ==========================================
# 2. METODO RUNGE-KUTTA DE ORDEN 4
# ==========================================

def rk4(theta, omega, K, h):
    k1 = kuramoto(theta, omega, K)
    k2 = kuramoto(theta + h*k1/2, omega, K)
    k3 = kuramoto(theta + h*k2/2, omega, K)
    k4 = kuramoto(theta + h*k3, omega, K)

    return theta + (h/6)*(k1 + 2*k2 + 2*k3 + k4)


# ==========================================
# 3. PARAMETROS GENERALES
# ==========================================

N = 30
h = 0.0005
T = 5

tiempos = np.arange(0, T + h/2, h)

rng = np.random.default_rng(42)

theta0 = rng.uniform(0, 2*np.pi, N)
u = rng.uniform(0, 1, N)


# ==========================================
# 4. ESCENARIOS CEREBRALES
# ==========================================

rangos = {
    "Meditacion": (8, 12),
    "Estres": (23, 30),
    "Ansiedad": (13, 30),
    "Esfuerzo cognitivo": (4, 7)
}

escenarios = {}

for nombre, (f_min, f_max) in rangos.items():

    frecuencias = f_min + (f_max - f_min)*u
    omega = 2*np.pi*frecuencias

    escenarios[nombre] = omega


# ==========================================
# 5. SIMULACION CON RK4
# ==========================================

def simular(omega, K):
    fases = np.zeros((len(tiempos), N))
    fases[0] = theta0

    for i in range(1, len(tiempos)):
        fases[i] = rk4(fases[i-1], omega, K, h)

    return fases


# ==========================================
# 6. PARAMETRO DE ORDEN
# ==========================================

def sincronizacion(fases):
    return np.abs(np.mean(np.exp(1j*fases), axis=1))


# ==========================================
# 7. COMPARACION CON K FIJO
# ==========================================

K = 10

plt.figure(figsize=(10, 6))

for nombre, omega in escenarios.items():

    fases = simular(omega, K)
    r = sincronizacion(fases)

    promedio = np.mean(r)

    print(
        f"{nombre}: "
        f"sincronizacion promedio = {promedio:.4f}"
    )

    plt.plot(tiempos, r, label=nombre)

plt.xlabel("Tiempo (s)")
plt.ylabel("Parametro de orden r(t)")
plt.title("Sincronizacion de los cuatro escenarios")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_1_tiempo.png", dpi=300)
plt.close()

# ==========================================
# 8. COMPARACION VARIANDO K
# ==========================================

valores_K = np.linspace(0, 120, 25)

plt.figure(figsize=(10, 6))

for nombre, omega in escenarios.items():

    promedios = []

    for K in valores_K:

        fases = simular(omega, K)
        r = sincronizacion(fases)

        # Promedio durante el ultimo segundo
        promedio = np.mean(r[tiempos >= T-1])

        promedios.append(promedio)

    plt.plot(
        valores_K,
        promedios,
        marker="o",
        label=nombre
    )

plt.xlabel("Acoplamiento K (rad/s)")
plt.ylabel("Sincronizacion promedio final")
plt.title("Sincronizacion en funcion de K")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafica_2_acoplamiento.png", dpi=300)
plt.close()

print("Segunda gráfica guardada correctamente")



# ==========================================
# 9. ANIMACION DE LOS CUATRO ESCENARIOS
# ==========================================

from matplotlib.animation import FuncAnimation, PillowWriter

K_anim = 30

nombres = list(escenarios.keys())

# Calcular las fases con RK4
resultados = {}

for nombre, omega in escenarios.items():
    resultados[nombre] = simular(omega, K_anim)

# Usar aproximadamente 150 fotogramas
indices = np.linspace(
    0, len(tiempos) - 1, 150, dtype=int
)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

puntos = []
vectores = []
etiquetas = []

colores = ["blue", "red", "purple", "green"]

for ax, nombre, color in zip(axes, nombres, colores):

    circulo = plt.Circle(
        (0, 0), 1, fill=False, color="gray"
    )

    ax.add_patch(circulo)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.set_title(nombre)
    ax.axis("off")

    p, = ax.plot([], [], "o", color=color)
    v, = ax.plot([], [], "-", color="orange", lw=3)

    etiqueta = ax.text(
        0, -1.12, "",
        ha="center", fontsize=11
    )

    puntos.append(p)
    vectores.append(v)
    etiquetas.append(etiqueta)


def actualizar(frame):

    indice = indices[frame]
    t = tiempos[indice]

    for i, nombre in enumerate(nombres):

        theta = resultados[nombre][indice]
        omega = escenarios[nombre]

        # Marco giratorio: elimina la rotacion media
        # sin modificar el valor de sincronizacion
        theta = theta - np.mean(omega) * t

        x = np.cos(theta)
        y = np.sin(theta)

        puntos[i].set_data(x, y)

        # Vector de sincronizacion colectiva
        z = np.mean(np.exp(1j * theta))
        r = np.abs(z)

        vectores[i].set_data(
            [0, np.real(z)],
            [0, np.imag(z)]
        )

        etiquetas[i].set_text(f"r(t) = {r:.3f}")

    fig.suptitle(
        f"Kuramoto | K = {K_anim} | t = {t:.2f} s",
        fontsize=14
    )

    return puntos + vectores + etiquetas


animacion = FuncAnimation(
    fig,
    actualizar,
    frames=len(indices),
    interval=70,
    blit=False
)

animacion.save(
    "animacion_estados.gif",
    writer=PillowWriter(fps=5)
)

plt.close(fig)

print("Animacion guardada: animacion_estados.gif")
