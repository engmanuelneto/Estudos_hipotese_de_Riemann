import numpy as np
import matplotlib.pyplot as plt

gamma = 14.134725141

x = np.linspace(2,1000,10000)

t = np.log(x)

y = np.cos(gamma*t)

Y = np.fft.rfft(y)

freq = np.fft.rfftfreq(len(y), d=(t[1]-t[0]))

plt.figure(figsize=(12,6))

plt.plot(freq, np.abs(Y))

plt.axvline(
    gamma/(2*np.pi),
    color="red",
    linestyle="--",
    label=f'γ/(2π)={gamma/(2*np.pi):.3f}'
)

plt.xlabel("Frequência")
plt.ylabel("Amplitude FFT")
plt.title("FFT da oscilação associada ao primeiro zero")

plt.legend()
plt.grid()

plt.show()