import math

def g(x):
    return math.sin(x)**2 + 1

def ste(p0, epsilon):
    p1 = None
    p2 = None
    pg = None
    pg_anterior = None
    error = None
    itr_n = 0

    # Calcular el pgorro inicial
    p1 = g(p0)
    p2 = g(p1)
    pg = p0 - ((p1 - p0)**2) / (p2 - 2 * p1 + p0)

    # Ya que es el primero, no se puede calcular el error
    print("{} & {: .10f} & {: .10f} & {: .10f} & {: .10f} & - \\\\".format(itr_n, p0, p1, p2, pg))
    while True:

        itr_n = itr_n + 1
        pg_anterior = pg

        # Se mejora p_0 con el pgorro anterior
        p0 = pg
        p1 = g(p0)
        p2 = g(p1)

        # Formula de Aitken
        pg = p0 - ((p1 - p0)**2) / (p2 - 2 * p1 + p0)

        # Error entre aproximaciones de pgorro
        error = math.fabs(pg - pg_anterior)

        print("{} | {: .10f} | {: .10f} | {: .10f} | {: .10f} | {: e} ".format(itr_n,p0,p1,p2,pg,error))
        if(error < epsilon):
            break