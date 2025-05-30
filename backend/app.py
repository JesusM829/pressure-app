from flask import Flask, render_template, request, jsonify
import numpy as np
from bisection import bisection
from newton import newton

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No se recibió ningún JSON válido'}), 400

        P1 = float(data['P1'])
        f = float(data['f'])
        L = float(data['L'])
        D = float(data['D'])
        Q = float(data['Q'])
        g = float(data['g'])
        method = data['method']

        if method == 'bisection':
            root, it, err = bisection(P1, f, L, D, Q, g)
        elif method == 'newton':
            root, it, err = newton(P1, f, L, D, Q, g)
        elif method == 'compare':
            b_root, b_it, b_err = bisection(P1, f, L, D, Q, g)
            n_root, n_it, n_err = newton(P1, f, L, D, Q, g)
            return jsonify({
                'bisection': {'root': b_root, 'iterations': b_it, 'error': b_err},
                'newton': {'root': n_root, 'iterations': n_it, 'error': n_err}
            })
        else:
            return jsonify({'error': 'Método inválido'}), 400

        # f(P) para graficar
        P_vals = np.linspace(0, P1 * 2, 200).tolist()
        f_vals = [P1 - P - (f * L / (2 * g * D)) * (Q**2 / (np.pi**2 * D**4)) for P in P_vals]

        return jsonify({
            'root': round(root, 6),
            'iterations': it,
            'error': err,
            'P_vals': P_vals,
            'f_vals': f_vals
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
