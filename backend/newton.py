def newton(P1, f, L, D, Q, g, tol=1e-6, max_iter=1000):
    from math import pi

    def fn(P):
        return P1 - P - (f * L / (2 * g * D)) * (Q**2 / (pi**2 * D**4))

    def dfn(P):
        return -1  # derivada constante

    x0 = P1
    iter_count = 0

    while iter_count < max_iter:
        x1 = x0 - fn(x0) / dfn(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
        iter_count += 1

    root = x1
    err = abs((x1 - x0) / root)
    return root, iter_count, err
