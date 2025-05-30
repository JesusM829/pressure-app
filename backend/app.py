import os

# Define primero la variable de entorno de Octave (omite esta línea en Mac si Octave ya está en PATH)
# os.environ['OCTAVE_EXECUTABLE'] = '/usr/local/bin/octave'  # Solo si es necesario

from flask import Flask, render_template, request, jsonify
from oct2py import Oct2Py
import numpy as np
import matplotlib.pyplot as plt

# Inicializar Oct2Py
oc = Oct2Py()

# Crear instancia Flask
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

        # Extraer parámetros del cuerpo JSON
        P1, f, L, D, Q, g = [float(data[k]) for k in ('P1','f','L','D','Q','g')]
        method = data['method']

        # Agregar ruta de scripts .m
        oc.addpath(os.path.join(app.root_path, 'octave'))

        # Ejecutar método numérico
        if method == 'bisection':
            root, it, err = oc.bisection(P1, f, L, D, Q, g, nout=3)
        else:
            root, it, err = oc.newton(P1, f, L, D, Q, g, nout=3)

        # Convertir a tipos de Python
        root, it, err = float(root), int(it), float(err)

        # Generar datos para graficar la función f(P)
        P_vals = np.linspace(0, P1*2, 200).tolist()
        f_vals = [P1 - P - (f*L/(2*g*D))*(Q**2/(np.pi**2*D**4)) for P in P_vals]

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
    