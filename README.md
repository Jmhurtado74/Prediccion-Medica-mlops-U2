# Predicción Médica Simulada – MLOps (Unidad 2)

Este repositorio corresponde al taller de la **Unidad 2** del curso  
**Machine Learning Operations (MLOps)** de la Maestría en Inteligencia Artificial Aplicada – Universidad Icesi.

El objetivo es versionar y automatizar una solución sencilla de predicción de estados de salud en pacientes,
utilizando buenas prácticas de:

- Control de versiones con **Git y GitHub**
- Manejo de ramas y **Pull Requests**
- Contenerización con **Docker**
- Automatización con **GitHub Actions** (CI/CD)

---

## 🩺 Descripción del problema

Se simula un sistema de apoyo a la decisión médica que, a partir de variables básicas del paciente:

- Edad
- Temperatura corporal (fiebre)
- Presencia de dolor

estima de forma aproximada el posible **estado de salud** del paciente mediante una lógica de reglas
(simulación de un modelo de clasificación).

El sistema devuelve categorías como:

- SIN ENFERMEDAD / NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD AGUDA (RIESGO ALTO)
- ENFERMEDAD CRÓNICA  
- (Unidad 2) **ENFERMEDAD TERMINAL** y reporte de estadísticas de uso

---

## 🧱 Estructura general del repositorio

La estructura objetivo del repositorio es:

```text
prediccion-medica-mlops-U2/
├── app.py                # Aplicación Flask que simula el modelo
├── Dockerfile            # Imagen Docker para el despliegue
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación principal
├── templates/
│   └── index.html        # Interfaz web para el médico
├── data/
│   └── predicciones.log  # Registro de predicciones (se genera en ejecución)
└── tests/
    └── test_app.py       # Pruebas unitarias para el pipeline de CI/CD
