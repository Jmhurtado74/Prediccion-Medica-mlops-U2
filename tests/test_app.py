import os
import sys

# =========================================================================
# Ajuste del path para que Python pueda importar app.py correctamente
# =========================================================================

# Directorio donde está este archivo de prueba
TEST_DIR = os.path.dirname(os.path.abspath(__file__))

# Carpeta raíz del proyecto (un nivel arriba de tests/)
PROJECT_ROOT = os.path.abspath(os.path.join(TEST_DIR, ".."))

# Agregar ruta del proyecto a sys.path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Ahora sí se puede importar app.py correctamente
from app import app, LOG_FILE


# =========================================================================
# Funciones auxiliares
# =========================================================================

def limpiar_log():
    """Elimina el archivo de log para que cada prueba comience limpia."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)


# =========================================================================
# Pruebas
# =========================================================================

def test_prediccion_enfermedad_leve():
    """
    PRUEBA 1:
    - Se envía un formulario simulando un paciente joven con fiebre moderada.
    - Se espera que el diagnóstico contenga 'ENFERMEDAD LEVE'.
    """
    limpiar_log()
    cliente = app.test_client()

    respuesta = cliente.post(
        "/predecir",
        data={
            "edad": "25",
            "fiebre": "37.5",
            "dolor": "1"
        }
    )

    texto = respuesta.get_data(as_text=True)

    assert respuesta.status_code == 200
    assert "ENFERMEDAD LEVE" in texto


def test_reporte_muestra_ultima_prediccion():
    """
    PRUEBA 2:
    - Se crea una predicción (que debe registrarse en el log).
    - Luego se llama a /reporte.
    - Se debe ver el texto 'Reporte de predicciones' y al menos una categoría.
    """
    limpiar_log()
    cliente = app.test_client()

    # Hacemos una predicción
    cliente.post(
        "/predecir",
        data={
            "edad": "75",
            "fiebre": "40.5",
            "dolor": "1"
        }
    )

    # Consultamos el reporte
    respuesta = cliente.get("/reporte")
    texto = respuesta.get_data(as_text=True)

    assert respuesta.status_code == 200
    assert "Reporte de predicciones" in texto
    assert "ENFERMEDAD" in texto






















