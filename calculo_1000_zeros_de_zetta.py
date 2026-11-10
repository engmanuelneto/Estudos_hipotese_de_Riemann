import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero
import os

# =====================================================
# CONFIGURAÇÃO
# =====================================================

N_ZEROS = 1000
ARQUIVO = "zeros_zeta_1000.npy"

# =====================================================
# CARREGA OU CALCULA OS ZEROS
# =====================================================

if os.path.exists(ARQUIVO):

    print("Carregando zeros salvos...")

    gammas = np.load(ARQUIVO)

else:

    print("Calculando os 1000 primeiros zeros...")
    print("Isso pode levar vários minutos.\n")

    lista = []

    for n in range(1, N_ZEROS + 1):

        gamma = float(zetazero(n).imag)

        lista.append(gamma)

        if n % 50 == 0:
            print(f"{n} zeros calculados")

    gammas = np.array(lista)

    np.save(ARQUIVO, gammas)

    print("\nArquivo salvo.")

# =====================================================
# ESTATÍSTICAS
# =====================================================

spacing = np.diff(gammas)

media = np.mean(spacing)
desvio = np.std(spacing)

print("\n===== ESTATÍSTICAS =====")

print(f"Número de zeros: {len(gammas)}")
print(f"Primeiro zero: {gammas[0]:.6f}")
print(f"Último zero: {gammas[-1]:.6f}")

print(f"\nEspaçamento médio: {media:.6f}")
print(f"Desvio padrão: {desvio:.6f}")

# =====================================================
# FFT
# =====================================================

spacing_centralizado = spacing - media

fft = np.fft.rfft(spacing_centralizado)

freq = np.fft.rfftfreq(
    len(spacing_centralizado),
    d=1
)

amplitude = np.abs(fft)

# =====================================================
# PICOS ESPECTRAIS
# =====================================================

indices = np.argsort(amplitude)[::-1]

print("\n===== MAIORES PICOS =====\n")

contador = 0

for idx in indices:

    if idx == 0:
        continue

    print(
        f"Frequência = {freq[idx]:.5f} | "
        f"Amplitude = {amplitude[idx]:.5f}"
    )

    contador += 1

    if contador == 10:
        break

# =====================================================
# GRÁFICO 1
# =====================================================

fig1 = plt.figure(figsize=(12, 6))

plt.plot(
    np.arange(1, len(gammas)+1),
    gammas,
    linewidth=1.5
)

plt.title(
    "Primeiros 1000 zeros não triviais"
)

plt.xlabel("Índice n")
plt.ylabel("γₙ")

plt.grid(True)

# =====================================================
# GRÁFICO 2
# =====================================================

fig2 = plt.figure(figsize=(12, 6))

plt.plot(
    spacing,
    linewidth=1
)

plt.title(
    "Espaçamentos entre zeros consecutivos"
)

plt.xlabel("n")
plt.ylabel("γₙ₊₁ − γₙ")

plt.grid(True)

# =====================================================
# GRÁFICO 3
# =====================================================

fig3 = plt.figure(figsize=(12, 6))

plt.hist(
    spacing,
    bins=40,
    density=True,
    alpha=0.75
)

plt.title(
    "Distribuição dos espaçamentos"
)

plt.xlabel("Espaçamento")
plt.ylabel("Densidade")

plt.grid(True)

# =====================================================
# GRÁFICO 4
# =====================================================

fig4 = plt.figure(figsize=(12, 6))

plt.plot(
    freq,
    amplitude,
    linewidth=1
)

plt.title(
    "Espectro de Fourier dos espaçamentos"
)

plt.xlabel("Frequência normalizada")
plt.ylabel("Amplitude")

plt.xlim(0, 0.5)

plt.grid(True)

# =====================================================
# MOSTRA TODOS AO FINAL
# =====================================================

plt.show()
