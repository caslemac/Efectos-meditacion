from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

salida = Path(__file__).resolve().parent / 'resultados' / 'graficas'
salida.mkdir(parents=True, exist_ok=True)

# Ondas ideales: solo ilustran la frecuencia, NO son registros de EEG
fs = 500
t = np.arange(0, 1, 1/fs)
bandas = [('Delta', 2), ('Theta', 6), ('Alfa', 10), ('Beta', 20), ('Gamma', 40)]
colores = ['#0072B2', '#009E73', '#D55E00', '#CC79A7', '#E69F00']
fig, axes = plt.subplots(5, 1, figsize=(10, 8), sharex=True)
for ax, (nombre, frecuencia), color in zip(axes, bandas, colores):
    senal = np.sin(2*np.pi*frecuencia*t)
    ax.plot(t, senal, lw=1.4, color=color)
    ax.set_ylabel(f'{nombre}\n{frecuencia} Hz', rotation=0, labelpad=35, va='center')
    ax.set_ylim(-1.25, 1.25)
    ax.grid(alpha=.2)
axes[-1].set_xlabel('Tiempo (s)')
fig.suptitle('Bandas de frecuencia EEG — ondas sintéticas ideales')
fig.tight_layout()
fig.savefig(salida / 'bandas_eeg_sinteticas.png', dpi=180)
plt.close(fig)

# Ejemplo hipotético: ambas condiciones tienen la MISMA frecuencia de 10 Hz.
# Solo cambia la dispersión de las fases de tres señales.
t = np.arange(0, .5, 1/fs)
f = 10
fases_disp = [0, 2.0, 4.0]
fases_alin = [0, .2, .4]
fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
for ax, fases, titulo in zip(axes, [fases_disp, fases_alin],
                             ['Condición A: fases dispersas (hipotética)',
                              'Condición B: fases más alineadas (hipotética)']):
    for i, phi in enumerate(fases, start=1):
        ax.plot(t, np.sin(2*np.pi*f*t+phi), label=f'Señal {i}', lw=1.6)
    r = abs(np.mean(np.exp(1j*np.array(fases))))
    ax.set_title(f'{titulo} | r = {r:.3f}')
    ax.set_ylabel('Amplitud (u.a.)')
    ax.set_ylim(-1.3,1.3)
    ax.legend(loc='upper right', ncol=3, fontsize=9)
    ax.grid(alpha=.2)
axes[-1].set_xlabel('Tiempo (s)')
fig.suptitle('Ejemplo didáctico de coherencia de fases — NO son EEG reales')
fig.tight_layout()
fig.savefig(salida / 'fases_eeg_hipoteticas.png', dpi=180)
plt.close(fig)
print('Gráficas guardadas en:', salida)
