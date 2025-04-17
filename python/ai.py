import math

def gx(x):
    return 1 + math.sin(x)**2

def ai(p0, epsilon):
    # Calcular el pgorro inicial
    p1 = gx(p0)
    p2 = gx(p1)
    pg = p0 - ((p1 - p0)**2) / (p2 - 2 * p1 + p0)
    itr_n = 0
    pg_anterior = None
    error = None

    # Ya que es el primero, no se puede calcular el error
    print("{:3} & {: .10f} & {: .10f} & {: .10f} & {: .10f} & - \\\\".format(itr_n, p0, p1, p2, pg))
    while True:

        itr_n = itr_n + 1
        pg_anterior = pg

        p0 = p1
        p1 = p2
        p2 = gx(p1)

        # Formula de Aitken
        pg = p0 - ((p1 - p0)**2) / (p2 - 2 * p1 + p0)

        # Error entre aproximaciones de pgorro
        error = math.fabs(pg - pg_anterior)

        print("{:3} | {: .10f} | {: .10f} | {: .10f} | {: .10f} | {: e} ".format(itr_n,p0,p1,p2,pg,error))
        if(error < epsilon):
            break

ai(1, math.pow(10, -3))