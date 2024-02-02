import random

#EJERCICIO 1
def integral(n):
    #func = x**2 + 2
    area = (2 * n**3 + 3 * n**2 + n)/ (6 * n**3) + 1/n + 4
    return area

print(integral(5))
#----------------------------------

#EJERCICIO 2
def integral2(n):
    #func = x
    area = 1+(n+1)/ (2*n)
    return area

print(integral2(5))

def areaBetween(n):
    return integral(n)-integral2(n)
print(areaBetween(5))
#----------------------------------

#EJERCICIO 3
def suma(n):
    result = 0
    a=random.randint(0,n)
    result += a
    b=random.randint(0,a)
    result += b
    c = n-result
    result += c
    return a,b,c

print(suma(10))
#----------------------------------