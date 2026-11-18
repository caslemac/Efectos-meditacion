# Meditation Effects

### Paola Castillo Camacho

### Affiliations

- Autonomous University of Mexico (UNAM)

- National School of Higher Studies (ENES)

## Description 

For this project, I want to model how meditation affects our body, especially the brain.
To do it, I investigated two different models:

## Kuramoto Model (phase synchronization):

A mathematical model describing how a group of oscillators (like brain waves) synchronize over time. It is used to represent how meditation can increase coherence between different brain regions.

**Governing equation**

$$
\frac{d\theta_i}{dt} = \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j - \theta_i), \quad i = 1,\dots,N
$$

- $\theta_i(t)$: phase of oscillator $i$ (radians)
- $\omega_i$: natural frequency of oscillator $i$, usually drawn from a distribution $g(\omega)$ (e.g., Gaussian)
- $K$: coupling strength between oscillators
- $N$: number of oscillators
- $\sin(\theta_j - \theta_i)$: pulls oscillator  $i$  toward the phase of oscillator  $j$

**Order parameter (measure of synchrony)**

$$
r(t)\,e^{i\psi(t)} = \frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j(t)}
$$

- $r \in [0,1]$:  $r \approx 0$ means incoherent (desynchronized),  $r \approx 1$ means fully synchronized
- $\psi$: average phase of the population

**Mean-field form** 

$$
\frac{d\theta_i}{dt} = \omega_i + K\,r\,\sin(\psi - \theta_i)
$$

**Critical coupling** (for a symmetric, unimodal $g(\omega)$ ): synchronization emerges when

$$
K > K_c = \frac{2}{\pi\, g(0)}
$$

---

**References**
- Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-linear oscillators. *Lecture Notes in Physics*, 39, 420–422.
- Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence*. Springer.
- Strogatz, S. H. (2000). From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators. *Physica D*, 143, 1–20.
- Acebrón, J. A. et al. (2005). The Kuramoto model: A simple paradigm for synchronization phenomena. *Reviews of Modern Physics*, 77, 137–185.
- Breakspear, M., Heitmann, S., & Daffertshofer, A. (2010). Generative models of cortical oscillations. *Frontiers in Human Neuroscience*, 4, 190.
- Wilson, H. R., & Cowan, J. D. (1972). Excitatory and inhibitory interactions in localized populations of model neurons. *Biophysical Journal*, 12(1), 1–24.
- Wilson, H. R., & Cowan, J. D. (1973). A mathematical theory of the functional dynamics of cortical and thalamic nervous tissue. *Kybernetik*, 13(2), 55–80.
- Ermentrout, G. B., & Terman, D. H. (2010). *Mathematical Foundations of Neuroscience*. Springer.
- Cowan, J. D., Neuman, J., & van Drongelen, W. (2016). Wilson–Cowan equations for neocortical dynamics. *Journal of Mathematical Neuroscience*, 6, 1.
- Cabral, J., Hugues, E., Sporns, O., & Deco, G. (2011). Role of local network oscillations in resting-state functional connectivity. *NeuroImage*, 57(1), 130–139.
