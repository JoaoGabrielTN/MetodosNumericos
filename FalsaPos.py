from typing import Callable

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def Fx(x: float) -> float:
    return round(x**3+2*x-1, 3)

def Xki(a: float, b: float, erro: int, fx: Callable) -> float:
    result = (a * fx(b) - b*fx(a))/(fx(b) - fx(a))
    abss = abs(fx(result))
    while(abss >= 10**erro):
        a = result
        result = (a * fx(b) - b*fx(a))/(fx(b) - fx(a))
        abss = abs(fx(result))
    return truncate(result, 3)

print(Xki(0, 1, -3, Fx))