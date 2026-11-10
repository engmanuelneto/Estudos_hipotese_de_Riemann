import numpy as np
import matplotlib.pyplot as plt
from sympy import primepi
from scipy.special import expi

# =====================================================
# Primeiros zeros não triviais da função zeta
# =====================================================

zeros = np.array([
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

# =====================================================
# Integral Logarítmica Li(x)
# =====================================================

def li(x):
    """
    Li(x) ≈ Ei(log(x))
    """
    x = np.asarray(x, dtype=float)
    return expi(np.log(x))

# =====================================================
# Aproximação via fórmula explícita de Riemann
# =====================================================

def riemann_explicit(x, zeros):

    x = np.asarray(x, dtype=float)

    resultado = li(x)

    soma = np.zeros_like(x, dtype=float)

    for gamma in zeros:

        rho = 0.5 + 1j * gamma

        termo = np.real(
            np.exp(rho * np.log(x))
            / (rho * np.log(x))
        )

        soma += termo

    resultado = resultado - 2 * soma

    return resultado

# =====================================================
# Domínio de análise
# =====================================================

x = np.arange(10, 1001)

# =====================================================
# π(x) real
# =====================================================

pi_real = np.array([
    int(primepi(int(v)))
    for v in x
])

# =====================================================
# Aproximações
# =====================================================

li_aprox = li(x)

riemann_aprox = riemann_explicit(
    x,
    zeros
)

# =====================================================
# Erros
# =====================================================

erro_li = np.abs(
    pi_real - li_aprox
)

erro_riemann = np.abs(
    pi_real - riemann_aprox
)

# =====================================================
# Tabela resumo
# =====================================================

print("\nComparação em alguns pontos:\n")

for ponto in [100, 200, 500, 1000]:

    real = int(primepi(ponto))

    li_val = float(
        li(np.array([ponto]))[0]
    )

    rie_val = float(
        riemann_explicit(
            np.array([ponto]),
            zeros
        )[0]
    )

    print(
        f"x={ponto:4d} | "
        f"π(x)={real:4d} | "
        f"Li(x)={li_val:9.2f} | "
        f"Riemann={rie_val:9.2f}"
    )

# =====================================================
# Gráfico 1
# =====================================================

plt.figure(figsize=(14, 7))

plt.plot(
    x,
    pi_real,
    color="black",
    linewidth=3,
    label="π(x) real"
)

plt.plot(
    x,
    li_aprox,
    linestyle="--",
    linewidth=2,
    label="Li(x)"
)

plt.plot(
    x,
    riemann_aprox,
    linewidth=2,
    label="Fórmula Explícita de Riemann"
)

plt.title(
    "Distribuição dos Números Primos"
)

plt.xlabel("x")
plt.ylabel("Quantidade de primos ≤ x")

plt.legend()
plt.grid(True)

# =====================================================
# Gráfico 2
# =====================================================

plt.figure(figsize=(14, 7))

plt.plot(
    x,
    erro_li,
    linewidth=2,
    label="Erro Li(x)"
)

plt.plot(
    x,
    erro_riemann,
    linewidth=2,
    label="Erro Fórmula de Riemann"
)

plt.title(
    "Erro das Aproximações"
)

plt.xlabel("x")
plt.ylabel("Erro Absoluto")

plt.legend()
plt.grid(True)

# =====================================================
# Estatísticas finais
# =====================================================

print("\nErro médio:\n")

print(
    f"Li(x): {erro_li.mean():.3f}"
)

print(
    f"Riemann: {erro_riemann.mean():.3f}"
)

# =====================================================
# Mostra TODOS os gráficos apenas no final
# =====================================================

plt.show()