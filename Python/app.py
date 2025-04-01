# Importamos las librerías necesarias de Flask
from flask import Flask, request, jsonify, render_template

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

def multiplicar_matrices(matriz1, matriz2):
    """
    Función para multiplicar dos matrices.
    Recibe dos matrices en forma de listas de listas y devuelve el resultado como un diccionario.
    """
    # Obtenemos las dimensiones de las matrices
    filasA, columnasA = len(matriz1), len(matriz1[0])  # Dimensiones de la primera matriz
    filasB, columnasB = len(matriz2), len(matriz2[0])  # Dimensiones de la segunda matriz

    # Verificamos que las matrices sean compatibles para la multiplicación (columnas de A = filas de B)
    if columnasA != filasB:
        return {"error": "Las matrices no se pueden multiplicar"}  # Devolvemos un error en caso de incompatibilidad

    # Creamos la matriz resultado usando comprensión de listas
    resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(columnasA)) for j in range(columnasB)] for i in range(filasA)]

    return {"resultado": resultado}  # Retornamos el resultado en formato JSON

# Ruta principal que renderiza el archivo HTML
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el archivo HTML en la carpeta 'templates'

# Ruta para multiplicar matrices mediante una petición POST
@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    # Recibimos los datos enviados en formato JSON
    data = request.json
    matriz1 = data.get("matriz1")  # Extraemos la primera matriz del JSON recibido
    matriz2 = data.get("matriz2")  # Extraemos la segunda matriz del JSON recibido

    # Verificamos que ambas matrices estén presentes
    if not matriz1 or not matriz2:
        return jsonify({"error": "Faltan matrices"}), 400  # Retornamos un error si falta alguna matriz

    # Llamamos a la función para multiplicar las matrices
    resultado = multiplicar_matrices(matriz1, matriz2)

    # Devolvemos el resultado en formato JSON
    return jsonify(resultado)

# Bloque principal para ejecutar la aplicación en modo depuración
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta el servidor con 'debug=True' para ver errores en tiempo real
