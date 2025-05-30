def bisection(P1, f, L, D, Q, g, tol=1e-6, max_iter=1000):
    from math import pi

    def fn(P):
        return P1 - P - (f * L / (2 * g * D)) * (Q**2 / (pi**2 * D**4))

    a, b = 0, P1 * 2
    fa, fb = fn(a), fn(b)
    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b]")

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        fc = fn(c)
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        iter_count += 1

    root = (a + b) / 2
    err = abs((b - a) / root)
    return root, iter_count, err
