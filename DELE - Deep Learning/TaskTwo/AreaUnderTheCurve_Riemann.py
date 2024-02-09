# --------------- PUNTO 1 ---------------
def riemann(n, a, b):
    dX = (b-a)/n
    area = 0
    for i in range(0, n):
        area += dX * func(a+ dX*i)
    return area

def func(x):
    result = x**2
    return result

print(riemann(5,2,3,))