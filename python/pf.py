import math

def g(x):
    return 1 + math.sin(x)**2

def pf(pn, epsilon):
    error = None
    g_pn = None
    itr_n = 0
    while True:
        g_pn = g(pn)
        error = math.fabs(g_pn - pn)
        print("{:3} | {: .10f} | {: .10f} | {: e}".format(itr_n, pn, g_pn, error))
        if error< epsilon or itr_n == 1000:
            break
        pn = g_pn
        itr_n = itr_n + 1

pf(1, math.pow(10, -3))