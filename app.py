import os
from datetime import datetime
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Archivo donde registramos las predicciones
LOG_FILE = os.getenv("LOG_FILE_PATH", "predicciones.log")

CATEGORIAS_VALIDAS = [
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD AGUDA (RIESGO ALTO)",
    "ENFERMEDAD CRÓNICA",
    "ENFERMEDAD TERMINAL"
]

def registrar_prediccion(edad, fiebre, dolor, estado):
    """
    Registra cada predicción en un archivo de texto.
    Formato simple: fecha|edad|fiebre|dolor|diagnostico
    """
    timestamp = datetime.now().isoformat()
    linea = f"{timestamp}|{edad}|{fiebre}|{dolor}|{estado}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linea)

def cargar_estadisticas():
    """
    Lee el archivo de log y calcula:
    - Conteo por categoría
    - Últimas 5 predicciones
    - Fecha de la última predicción
    """
    if not os.path.exists(LOG_FILE):
        return {
            "conteos": {cat: 0 for cat in CATEGORIAS_VALIDAS},
            "ultimas_5": [],
            "ultima_fecha": None
        }

    conteos = {cat: 0 for cat in CATEGORIAS_VALIDAS}
    registros = []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            try:
                ts, edad, fiebre, dolor, estado = linea.split("|")
                registros.append({
                    "timestamp": ts,
                    "edad": int(edad),
                    "fiebre": float(fiebre),
                    "dolor": int(dolor),
                    "estado": estado
                })
                if estado in conteos:
                    conteos[estado] += 1
            except ValueError:
                # Línea mal formada, se ignora
                continue

    registros_ordenados = sorted(
        registros,
        key=lambda r: r["timestamp"],
        reverse=True
    )

    ultimas_5 = registros_ordenados[:5]
    ultima_fecha = registros_ordenados[0]["timestamp"] if registros_ordenados else None

    return {
        "conteos": conteos,
        "ultimas_5": ultimas_5,
        "ultima_fecha": ultima_fecha
    }

def diagnosticar(edad, fiebre, dolor):
    """
    Lógica de diagnóstico con 5 categorías:
    - ENFERMEDAD LEVE
    - ENFERMEDAD AGUDA
    - ENFERMEDAD AGUDA (RIESGO ALTO)
    - ENFERMEDAD CRÓNICA
    - ENFERMEDAD TERMINAL
    Puedes ajustar estos umbrales si lo deseas,
    lo importante es que las 5 categorías se usen.
    """
    if fiebre < 37.5 and dolor == 0:
        estado = "ENFERMEDAD LEVE"
    elif 37.5 <= fiebre < 38.5:
        estado = "ENFERMEDAD AGUDA"
    elif 38.5 <= fiebre < 39.5:
        if edad > 60 or dolor == 1:
            estado = "ENFERMEDAD AGUDA (RIESGO ALTO)"
        else:
            estado = "ENFERMEDAD AGUDA"
    elif 39.5 <= fiebre < 40.5:
        estado = "ENFERMEDAD CRÓNICA"
    else:
        # fiebre muy alta (>= 40.5) se considera TERMINAL en este ejercicio
        estado = "ENFERMEDAD TERMINAL"

    return estado

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predecir", methods=["POST"])
def predecir():
    try:
        edad = int(request.form["edad"])
        fiebre = float(request.form["fiebre"])
        dolor = int(request.form["dolor"])

        estado = diagnosticar(edad, fiebre, dolor)

        # Registrar predicción
        registrar_prediccion(edad, fiebre, dolor, estado)

        return render_template(
            "index.html",
            resultado=f"Diagnóstico: {estado}"
        )
    except Exception as e:
        return f"Error en los datos ingresados: {e}", 400

@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    """
    Nueva funcionalidad: reporte de estadísticas
    - Conteo total de predicciones por categoría
    - Últimas 5 predicciones
    - Fecha de la última predicción
    """
    stats = cargar_estadisticas()
    # Puedes devolver HTML o JSON. Aquí las dos opciones:
    if request.args.get("formato")