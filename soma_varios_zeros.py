import numpy as np
import matplotlib.pyplot as plt

gammas = np.array([
14.134725141,
21.022039639,
25.010857580,
30.424876126,
32.935061588,
37.586178159,
40.918719012,
43.327073281,
48.005150881,
49.773832478
])

x = np.linspace(2,1000,20000)

t = np.log(x)

signal = np.zeros_like(t)

for g in gammas:
    signal += np.cos(g*t)/np.sqrt(g)

Y = np.fft.rfft(signal)

freq = np.fft.rfftfreq(
    len(signal),
    d=t[1]-t[0]
)

plt.figure(figsize=(12,6))

plt.plot(freq,np.abs(Y))

for g in gammas:
    plt.axvline(
        g/(2*np.pi),
        color="red",
        alpha=0.3
    )

plt.title(
    "Espectro de Fourier das oscilações dos zeros"
)

plt.xlabel("Frequência")
plt.ylabel("Amplitude")

plt.grid()

plt.show()