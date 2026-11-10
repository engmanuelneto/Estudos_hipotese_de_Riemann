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

real = [0.5] * len(gammas)

plt.figure(figsize=(8, 8))

plt.scatter(
    real,
    gammas,
    s=80,
    color="red"
)

plt.axvline(
    x=0.5,
    linestyle="--",
    color="black"
)

plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")

plt.title(
    "Primeiros zeros não triviais da função zeta"
)

plt.grid(True)

plt.show()