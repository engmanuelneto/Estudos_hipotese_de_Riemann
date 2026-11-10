import numpy as np
import matplotlib.pyplot as plt

# Primeiros zeros não triviais
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
    49.773832478,
]

# eixo x
x = np.linspace(2, 1000, 5000)

plt.figure(figsize=(14, 8))

for i, gamma in enumerate(gammas[:5]):

    y = np.cos(gamma * np.log(x))

    plt.plot(
        x,
        y,
        label=f"γ{i+1} = {gamma:.3f}"
    )

plt.title(
    "Oscilações produzidas pelos primeiros zeros da zeta"
)

plt.xlabel("x")
plt.ylabel("cos(γ log(x))")

plt.grid(True)
plt.legend()

plt.show()