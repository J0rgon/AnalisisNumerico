import math

def fx(x):
    return math.sin(x)**2 + 1

def bi(a, b, tol, n_max=1000):
    fa = fx(a)
    fb = fx(b)
    c = 0
    error = None

    if fa == 0:
        return {a, "Root in A"}
    elif fb == 0:
        return {b, "Root in B"}
    
    if fa*fb > 0:
        return {0, "Range not valid"}
    
    print("Iter |     a     |     b     |     c     |   f(a)   |   f(b)   |   f(c)   |  Error")
    print("----------------------------------------------------------------------------------")

    for i in range(n_max):

        c = (a+b)/2
        fc = fx(c)
        error = math.fabs((b-a)/2)

        print("{:4} | {:9.6f} | {:9.6f} | {:9.6f} | {:8.3e} | {:8.3e} | {:8.3e} | {:7.2e}".format(i, a, b, c, fa, fb, fc, error))

        if error < tol:
            return {c, 'Root found in c in {} iterations'.format(i+1)}

        if(fa*fc) > 0:
            a = c
            fa = fc
        
        if(fb*fc) > 0:
            b = c
            fb = fc
            
    return {c, "Reached max iterations, result may not be accurate"}
