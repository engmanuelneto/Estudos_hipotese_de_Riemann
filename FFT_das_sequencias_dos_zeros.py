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

espacamentos = np.diff(gammas)

Y = np.fft.rfft(
    espacamentos - np.mean(espacamentos)
)

freq = np.fft.rfftfreq(
    len(espacamentos)
)

plt.figure(figsize=(12,6))

plt.stem(freq,np.abs(Y))

plt.title(
    "FFT dos espaçamentos entre zeros da zeta"
)

plt.xlabel("Frequência")
plt.ylabel("Amplitude")

plt.grid()

plt.show()