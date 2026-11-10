import numpy as np
import matplotlib.pyplot as plt
from sympy import primepi
from scipy.special import sici

# Primeiros zeros não triviais da função zeta
# (parte imaginária)
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

def li(x):
    """
    Aproximação da Integral Logarítmica:
    Li(x) = Ei(ln(x))
    usando a relação com Si/Ci.
    """
    x = np.asarray(x, dtype=float)

    resultado = np.zeros_like(x)

    for i, xi in enumerate(x):
        n = 1000
        t = np.linspace(2, xi, n)
        y = 1 / np.log(t)
        resultado[i] = np.trapezoid(y, t)
    return resultado


def riemann_explicit(x, zeros):
    """
    Aproximação baseada na fórmula explícita de Riemann.

    π(x) ≈ Li(x)
           - 2 * Σ Re(Li(x^(1/2+iγ)))
    """

    soma = np.zeros_like(x, dtype=float)

    for gamma in zeros:

        rho = 0.5 + 1j * gamma

        termo = []

        for xi in x:

            z = np.exp(rho * np.log(xi))

            # Aproximação numérica de Li(z)
            li_complex = z / np.log(z)

            termo.append(np.real(li_complex))

        soma += np.array(termo)

    return li(x) - 2 * soma


# intervalo analisado
x = np.arange(10, 1000)

# valor real de π(x)
pi_real = np.array([primepi(int(v)) for v in x])

# aproximações
li_aprox = li(x)
riemann_aprox = riemann_explicit(x, zeros)

# ==========================
# gráfico principal
# ==========================

plt.figure(figsize=(12, 6))

plt.plot(x, pi_real,
         label="π(x) real",
         linewidth=3)

plt.plot(x, li_aprox,
         '--',
         label="Li(x)")

plt.plot(x, riemann_aprox,
         label="Fórmula Explícita de Riemann")

plt.xlabel("x")
plt.ylabel("Quantidade de primos ≤ x")
plt.title("Distribuição dos números primos")
plt.legend()
plt.grid(True)

plt.show()

# ==========================
# gráfico de erro
# ==========================

erro_li = np.abs(pi_real - li_aprox)
erro_riemann = np.abs(pi_real - riemann_aprox)

plt.figure(figsize=(12, 6))

plt.plot(x,
         erro_li,
         label="Erro da Li(x)")

plt.plot(x,
         erro_riemann,
         label="Erro da Fórmula de Riemann")

plt.xlabel("x")
plt.ylabel("Erro absoluto")
plt.title("Comparação dos erros")
plt.legend()
plt.grid(True)

plt.show()

# ==========================
# tabela resumo
# ==========================

print("\nComparação em alguns pontos:\n")

for ponto in [100, 200, 500, 1000]:

    real = primepi(ponto)

    li_val = li(np.array([ponto]))[0]

    rie_val = riemann_explicit(
        np.array([ponto]),
        zeros
    )[0]

    print(
        f"x={ponto:4d} | "
        f"π(x)={real:4d} | "
        f"Li={li_val:8.2f} | "
        f"Riemann={rie_val:8.2f}"
    )