# Meditation Effects

### Paola Castillo Camacho

### Affiliations

- Autonomous University of Mexico (UNAM)

- National School of Higher Studies (ENES)

## Description 

For this project, I want to model how meditation affects our body, especially the brain.

## Kuramoto Model (phase synchronization):

The Kuramoto model is a mathematical model, expressed as a system of coupled ordinary differential equations (ODEs), that describes how a group of oscillators (like brain waves) synchronize over time. Each oscillator has its own natural frequency, and the coupling between them pulls their phases together.

In this project, it is going to be used to represent how meditation can increase coherence between different brain regions. Since the system has no simple closed-form solution, it will be solved numerically using the fourth-order Runge-Kutta method (RK4).

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
## Brain Waves and EEG

Because this project will use EEG data extracted from several published studies, it is important to first define what an EEG is and which brain waves it records. For this explanation we will use hypothetical data, so that the results presented later in the project can be understood more easily.

Electroencephalography (EEG) records differences in electrical potential on the scalp, which reflect the combined activity of large populations of neurons. EEG signals are commonly studied by dividing them into frequency bands. The boundaries between bands are approximate and vary across studies.

| Band  | Approximate frequency | Common associations                                      |
|-------|-----------------------|----------------------------------------------------------|
| Delta | 0.5–4 Hz              | Deep sleep                                               |
| Theta | 4–8 Hz                | Drowsiness, memory, and certain meditative practices     |
| Alpha | 8–13 Hz               | Relaxed wakefulness, frequently with eyes closed         |
| Beta  | 13–30 Hz              | Cognitive and motor activity                             |
| Gamma | 30–80 Hz              | Sensory and cognitive processing                         |

## Phase Synchronization and Meditation

Two measures must be distinguished. **Band power** is the intensity of a signal within a given frequency range, whereas **phase synchronization** is the temporal alignment of the phases of different signals. A change in one does not necessarily imply a change in the other, so this project will analyze them separately.

## Frequency Selection

Initially, this project aimed to use real electroencephalography (EEG) data. However, the limited availability of open-access datasets and the lack of suitable recordings for the scenarios of interest made this approach difficult to implement.

Therefore, general brainwave frequency ranges associated with different mental and cognitive states were selected to simulate and analyze synchronization using the Kuramoto model.

| Scenario | Frequency Band | Proposed Range |
|---|---|---|
| Transcendental Meditation | Alpha | 8–12 Hz |
| Stress | High Beta | 23–30 Hz |
| Anxiety | Beta | 13–30 Hz |
| Cognitive Effort | Frontal Theta | 4–7 Hz |

The objective is to analyze how natural frequencies and coupling strength affect synchronization between oscillators.

It is important to emphasize that these frequency ranges represent a simplified approximation of brain activity. Therefore, the results are theoretical and exploratory rather than a direct representation of actual brain dynamics.







**References**

- OpenNeuro. Dataset ds003969, version 1.0.0. https://openneuro.org/datasets/ds003969/versions/1.0.0
- Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-linear oscillators. *Lecture Notes in Physics*, 39, 420–422.
- Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence*. Springer.
- Strogatz, S. H. (2000). From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators. *Physica D*, 143, 1–20.
- Acebrón, J. A. et al. (2005). The Kuramoto model: A simple paradigm for synchronization phenomena. *Reviews of Modern Physics*, 77, 137–185.
- Breakspear, M., Heitmann, S., & Daffertshofer, A. (2010). Generative models of cortical oscillations. *Frontiers in Human Neuroscience*, 4, 190.
- Ermentrout, G. B., & Terman, D. H. (2010). *Mathematical Foundations of Neuroscience*. Springer.
- Cabral, J., Hugues, E., Sporns, O., & Deco, G. (2011). Role of local network oscillations in resting-state functional connectivity. *NeuroImage*, 57(1), 130–139.
