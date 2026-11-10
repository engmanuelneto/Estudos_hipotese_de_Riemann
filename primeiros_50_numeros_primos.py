import math

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primos_ate(limite):
    return [n for n in range(2, limite + 1) if eh_primo(n)]

def li(x, n=10000):
    """
    Aproxima a integral logarítmica Li(x)
    usando integração numérica.
    """
    a = 2.0
    h = (x - a) / n
    soma = 0.0

    for i in range(n):
        t = a + i * h + h / 2
        soma += 1 / math.log(t)

    return soma * h

x = 1000

primos = primos_ate(x)
pi_x = len(primos)
li_x = li(x)

erro = abs(pi_x - li_x)
limite_rh = math.sqrt(x) * math.log(x)

print(f"π({x}) = {pi_x}")
print(f"Li({x}) = {li_x:.3f}")
print(f"Erro = {erro:.3f}")
print(f"Limite RH ≈ {limite_rh:.3f}")

print("\nPrimeiros 50 primos:")
print(primos[:50])