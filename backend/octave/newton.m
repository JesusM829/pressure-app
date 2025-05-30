function [root, iter, err] = newton(P1, f, L, D, Q, g)
    fn = @(P) P1 - P - (f*L/(2*g*D)) * (Q^2/(pi^2 * D^4));
    dfn = @(P) -1;
    x0 = P1; tol = 1e-6; iter = 0;
    while true
        x1 = x0 - fn(x0)/dfn(x0);
        iter = iter + 1;
        if abs(x1 - x0) < tol
            break;
        end
        x0 = x1;
    end
    root = x1; err = abs((x1 - x0)/root);
end
