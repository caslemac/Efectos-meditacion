import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

N = 5
omega = np.array([0.8, 0.9, 1.0, 1.1, 1.2])
theta0 = np.array([0.0, 0.5, 1.3, 2.0, 2.8])
h = 0.01
T = 20
pasos = int(T / h)
tiempos = np.linspace(0, T, pasos + 1)


def kuramoto(theta, omega, K):
    N = len(theta)
    dtheta = np.zeros(N)
    for i in range(N):
        influencia = 0.0
        for j in range(N):
            influencia += np.sin(theta[j] - theta[i])
        dtheta[i] = omega[i] + (K / N) * influencia
    return dtheta


def rk4(theta, omega, K, h):
    k1 = kuramoto(theta, omega, K)
    k2 = kuramoto(theta + h*k1/2, omega, K)
    k3 = kuramoto(theta + h*k2/2, omega, K)
    k4 = kuramoto(theta + h*k3, omega, K)
    return theta + h*(k1 + 2*k2 + 2*k3 + k4)/6


def simular(K):
    fases = np.zeros((pasos + 1, N))
    fases[0] = theta0
    for n in range(pasos):
        fases[n+1] = rk4(fases[n], omega, K, h)
    sincronizacion = np.abs(np.mean(np.exp(1j * fases), axis=1))
    return fases, sincronizacion



if __name__ == "__main__":

    salida = Path(__file__).resolve().parent / "resultados" / "graficas"
    salida.mkdir(parents=True, exist_ok=True)

    K = 0.5
    fases, r = simular(K)

    # Gráfica de fases
    plt.figure(figsize=(9, 5))

    for i in range(N):
        plt.plot(tiempos, fases[:, i], label=f"Oscilador {i+1}")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Fase acumulada (rad)")
    plt.title(f"Evolución de las fases - K = {K}")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(salida / "fases.png", dpi=180)
    plt.close()

    # Gráfica de sincronización
    plt.figure(figsize=(9, 5))
    plt.plot(tiempos, r)

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Sincronización r(t)")
    plt.title(f"Parámetro de orden - K = {K}")
    plt.ylim(0, 1.05)
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(salida / "sincronizacion.png", dpi=180)
    plt.close()

    # Comparación de acoplamientos
    plt.figure(figsize=(9, 5))

    for k in [0.0, 0.5, 1.5]:
        _, rk = simular(k)
        plt.plot(tiempos, rk, label=f"K = {k}")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Sincronización r(t)")
    plt.title("Comparación de valores de acoplamiento")
    plt.ylim(0, 1.05)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(salida / "comparacion_K.png", dpi=180)
    plt.close()

    print("Gráficas guardadas en:", salida)
    print("r(0):", round(r[0], 4))
    print("r(T):", round(r[-1], 4))
