import numpy as np
import matplotlib.pyplot as plt

def pi_x(x):
    """
    Retorna π(x): quantidade de primos <= x
    """
    if x < 2:
        return 0

    crivo = np.ones(x + 1, dtype=bool)
    crivo[0] = crivo[1] = False

    for p in range(2, int(np.sqrt(x)) + 1):
        if crivo[p]:
            crivo[p*p:x+1:p] = False

    return np.sum(crivo)

# Exemplo
x = 10000
print(f"π({x}) = {pi_x(x)}")
