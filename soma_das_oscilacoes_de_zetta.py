import numpy as np
import matplotlib.pyplot as plt

gammas = [
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
]

x = np.linspace(2, 5000, 10000)

onda_total = np.zeros_like(x)

for gamma in gammas:

    onda_total += np.cos(
        gamma * np.log(x)
    ) / np.sqrt(gamma)

plt.figure(figsize=(14, 8))

plt.plot(
    x,
    onda_total,
    color="navy",
    linewidth=2
)

plt.title(
    "Interferência dos primeiros zeros não triviais"
)

plt.xlabel("x")
plt.ylabel("Amplitude")

plt.grid(True)

plt.show()