import math
from typing import Callable

def Fx(x: float) -> float:
    return round(x**3 + 2*x**2 + x - 1, 4)

def DiffFx(x: float) -> float:
    return round(3*x**2 + 4*x + 1, 4)

def Xki(x: float, fx: Callable, diffFx: Callable) -> float:
    return round(x - fx(x)/diffFx(x), 4)

def NR(x0: float, erro: int, fx: Callable, diffFx: Callable) -> float:
    root = Xki(x0, fx, diffFx)
    while(abs(Fx(root)) >= 10**erro):
        root = Xki(root, fx, diffFx)
    return round(root, 4)

print(NR(0.625, -3, Fx, DiffFx))
