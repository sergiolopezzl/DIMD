def funcion(x):
    return x**3 + 3

def derivada(x):
    return 3 * x**2

def metodo_newton(funcion, derivada, x_inicial, tolerancia=1e-6, max_iter=10):
    x_actual = x_inicial
    iteracion = 0

    while abs(funcion(x_actual)) > tolerancia and iteracion < max_iter:
        x_actual = x_actual - funcion(x_actual) / derivada(x_actual)
        iteracion += 1

    if abs(funcion(x_actual)) <= tolerancia:
        return x_actual
    else:
        print("El método de Newton no convergió después de {} iteraciones.".format(max_iter))
        return None

# Punto de inicio para el método de Newton
x_inicial = 1.0

# Calcular la raíz usando el método de Newton
raiz = metodo_newton(funcion, derivada, x_inicial)

if raiz is not None:
    print("La raíz encontrada es:", raiz)
    print("El valor de la función en la raíz es:", funcion(raiz))
else:
    print("No se pudo encontrar la raíz.")
