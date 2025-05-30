# Pressure App

Aplicación web interactiva para el cálculo de presión en tuberías utilizando métodos numéricos como Bisección y Newton-Raphson. Incluye comparación de métodos, visualización de la función, y exportación de resultados.

## Características

- Cálculo numérico de la presión basada en ecuaciones no lineales.
- Elección entre los métodos: Bisección, Newton-Raphson o Comparar ambos.
- Visualización de la función \( f(P) \) con Plotly.
- Resultados exportables en formato CSV.

## Tecnologías

- **Frontend**: HTML, CSS, JavaScript, Bootstrap, Plotly.js
- **Backend**: Python 3, Flask, Oct2Py, GNU Octave
- **Despliegue**:
  - Frontend: Netlify
  - Backend: Render (opcional para producción)

## Instalación Local

### Requisitos
- Python 3
- GNU Octave
- pip

### Pasos

```bash
# Clonar el repositorio
https://github.com/tu_usuario/pressure-app.git
cd pressure-app

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r backend/requirements.txt

# Ejecutar servidor Flask
python backend/app.py
```

### Acceder a la app

Ir a `http://localhost:5000` en tu navegador.

## Estructura del Proyecto

```
pressure-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── octave/
│       ├── bisection.m
│       └── newton.m
├── frontend/
│   ├── index.html
│   ├── style.css
├── README.md
```

## Despliegue en Netlify

1. Crear una cuenta en [Netlify](https://netlify.app)
2. Ir a "Add new site" → "Deploy manually"
3. Subir carpeta `frontend/`
4. Netlify generará una URL gratuita para tu app web.

## Licencia

MIT © 2025 - Proyecto Final de Métodos Numéricos

## Autores

Equipo de Desarrollo - Ingeniería
- Backend: Jesus Martinez
- Frontend: Sebastian Teherean
- Cálculos: Jacith Mejia

---

Proyecto desarrollado como entrega final del curso de Métodos Numéricos con enfoque en SCRUM y aplicación web real.
