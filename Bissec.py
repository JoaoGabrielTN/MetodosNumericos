import math
def f1(x: float) -> float:
    """Returns f(x)"""
    return  x**5 + 2*x**3 + 2*x + 1

def f2(x: float) -> float:
    return math.cos(x) + math.log(x)

def f3(x: float) -> float:
    return x**3+2*x**2-x+1

def bis(a, b, erro, f):
    mid = round((a + b)/2, abs(erro))
    mod = abs(f(mid))
    while(mod >= 10**erro):
        if(f(a) < 0):
            if(f(mid) < 0):
                a = mid
            else: 
                b = mid
        else:
            if(f(mid) > 0):
                a = mid
            else: 
                b = mid
        mid = (a+b)/2
        mod = abs(f(mid))
    return round(mid, abs(erro))

print(bis(-3, -2, -4, f3))