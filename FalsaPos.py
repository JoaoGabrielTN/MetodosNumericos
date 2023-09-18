from typing import Callable

def Fx(x: float) -> float:
    return round(x**3+2*x-1, 3)

def Xki(a: float, b: float, erro: int, fx: Callable) -> float:
    result = (a * fx(b) - b*fx(a))/(fx(b) - fx(a))
    while(abs(fx(result)) >= 10**erro):
        if(fx(result) > 0):
            if(a > 0):
                a = result
            else:
                b = result
        else: 
            if(a < 0):
                a = result
            else:
                b = result
        result = (a * fx(b) - b*fx(a))/(fx(b) - fx(a))

    return round(result, 3)

print(Xki(0, 1, -3, Fx))