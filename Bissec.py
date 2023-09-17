import math
def func(x: float) -> float:
    """Returns f(x)"""
    return  x**5 + 2*x**3 + 2*x + 1

def bis(a, b, erro):
    mid = round((a + b)/2, abs(erro))
    mod = abs(func(mid))
    while(mod >= 10**erro):
        if(func(a) < 0):
            if(func(mid) < 0):
                a = round(mid, abs(erro))
            else: 
                b = round(mid, abs(erro))
        else:
            if(func(mid) > 0):
                a = round(mid, abs(erro))
            else: 
                b = round(mid, abs(erro))
        mid = round((a+b)/2, abs(erro))
        mod = abs(func(mid))
    return mid

print(bis(-1, 0, -2))