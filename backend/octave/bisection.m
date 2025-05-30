function [root, iter, err] = bisection(P1, f, L, D, Q, g)
    fn = @(P) P1 - P - (f*L/(2*g*D)) * (Q^2/(pi^2 * D^4));
    a = 0; b = P1*2;
    fa = fn(a); fb = fn(b);
    tol = 1e-6; iter = 0;
    while (b - a)/2 > tol
        c = (a + b)/2;
        fc = fn(c);
        if fa * fc < 0
            b = c; fb = fc;
        else
            a = c; fa = fc;
        end
        iter = iter + 1;
    end
    root = (a + b)/2;
    err = abs((b - a)/root);
end
