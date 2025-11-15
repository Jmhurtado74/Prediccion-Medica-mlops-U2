from flask import Flask, request, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# ============================
# Configuración de registro
# ============================

DATA_DIR = "data"
LOG_FILE = os.path.join(DATA_DIR, "predicciones.log")


def asegurar_directorio_data():
    """Crea el directorio 'data' si no existe."""
    os.makedirs(DATA_DIR, exist_ok=True)


def registrar_prediccion(edad: int, fiebre: float, dolor: int, estado: str) -> None:
    """
    Registra cada predicción en un archivo de texto para luego
    poder calcular estadísticas.

    Formato:
    fecha_iso;edad;fiebre;dolor;estado
    """
    asegurar_directorio_data()
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now().isoformat()};{edad};{fiebre};{dolor};{estado}\n"
        )


def obtener_estadisticas():
    """
    Lee el archivo de log y construye:
      - conteo_por_categoria: dict {categoria: cantidad}
      - ultimas_5: lista con las últimas 5 líneas del log
      - fecha_ultima: fecha de la última predicción registrada
    Si no existe el archivo, retorna valores vacíos.
    """
    if not os.path.exists(LOG_FILE):
        return {
            "conteo_por_categoria": {},
            "ultimas_5": [],
            "fecha_ultima": None,
        }

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lineas = [l.strip() for l in f.readlines() if l.strip()]

    conteo = {}
    for linea in lineas:
        partes = linea.split(";")
        if len(partes) != 5:
            continue
        _, _, _, _, estado = partes
        conteo[estado] = conteo.get(estado, 0) + 1

    ultimas_5 = lineas[-5:] if len(lineas) >= 5 else lineas
    fecha_ultima = None
    if lineas:
        ultima = lineas[-1].split(";")
        if len(ultima) == 5:
            fecha_ultima = ultima[0]

    return {
        "conteo_por_categoria": conteo,
        "ultimas_5": ultimas_5,
        "fecha_ultima": fecha_ultima,
    }


# ============================
# Rutas de la aplicación
# ============================

@app.route("/")
def home():
    """
    Página principal.
    Renderiza el formulario definido en templates/index.html
    """
    return render_template("index.html")


@app.route("/predecir", methods=["POST"])
def predecir():
    """
    Recibe los datos del formulario, aplica reglas simples de negocio
    para simular un modelo de predicción médica y devuelve un diagnóstico.

    Categorías posibles:
      - SIN ENFERMEDAD
      - ENFERMEDAD LEVE
      - ENFERMEDAD AGUDA
      - ENFERMEDAD AGUDA (RIESGO ALTO)
      - ENFERMEDAD CRÓNICA
      - ENFERMEDAD TERMINAL  (nueva categoría requerida en la Unidad 2)
    """
    try:
        edad = int(request.form["edad"])
        fiebre = float(request.form["fiebre"])
        dolor = int(request.form["dolor"])

        # ============================
        # Lógica de diagnóstico
        # ============================

        if fiebre < 37 and dolor == 0:
            estado = "SIN ENFERMEDAD"

        elif 37 <= fiebre < 38:
            estado = "ENFERMEDAD LEVE"

        elif 38 <= fiebre < 39:
            # Pacientes mayores con fiebre moderada → riesgo alto
            if edad > 60:
                estado = "ENFERMEDAD AGUDA (RIESGO ALTO)"
            else:
                estado = "ENFERMEDAD AGUDA"

        elif fiebre >= 40 and edad > 70:
            # Nueva categoría para la Unidad 2:
            # fiebre muy alta en personas mayores
            estado = "ENFERMEDAD TERMINAL"

        else:
            # Resto de casos se consideran crónicos
            estado = "ENFERMEDAD CRÓNICA"

        # Registrar la predicción en el archivo de log
        registrar_prediccion(edad, fiebre, dolor, estado)

        # Mantener el formato del resultado para el template
        mensaje = f"Diagnóstico: {estado}"
        return render_template("index.html", resultado=mensaje)

    except Exception as e:
        return f"Error en los datos ingresados: {e}"


@app.route("/reporte", methods=["GET"])
def reporte():
    """
    Nueva funcionalidad requerida:
    Devuelve estadísticas de uso del sistema:

      - Número total de predicciones realizadas por cada categoría
      - Últimas 5 predicciones registradas
      - Fecha de la última predicción

    El resultado se expone en formato JSON para que pueda ser
    consumido por otra vista, endpoint o herramienta.
    """
    stats = obtener_estadisticas()
    return render_template(
        'index.html',
        reporte=stats,
        resultado=None)
    #return jsonify(stats)


if __name__ == "__main__":
    # Configuración por defecto para ejecución local y en Docker
    app.run(host="0.0.0.0", port=5000)
