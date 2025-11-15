# Predicción Médica Simulada (MLOps - Docker + Flask)

Este proyecto forma parte del curso **Machine Learning Operations (MLOps)** de la Maestría en Inteligencia Artificial Aplicada – Universidad Icesi.  
Su objetivo es construir un pipeline reproducible que simule el comportamiento de un modelo médico capaz de diagnosticar, de forma aproximada, el estado de un paciente a partir de tres variables:

- **Edad del paciente**
- **Temperatura corporal (fiebre)**
- **Presencia de dolor**

La aplicación fue desarrollada con Flask y contenerizada con Docker, siguiendo las buenas prácticas de MLOps.  
Simula un modelo de clasificación médica simple que categoriza los resultados en varios estados posibles:

- **NIÑO SANO**
- **NO ENFERMO**
- **ENFERMEDAD LEVE**
- **ENFERMEDAD AGUDA**
- **ENFERMEDAD AGUDA (RIESGO ALTO)** cuando la fiebre es alta (≥ 38 °C) y la edad del paciente es avanzada (> 60 años)
- **ENFERMEDAD CRÓNICA**

De esta forma, la función del modelo y de la aplicación es apoyar, a modo de simulación, la priorización de pacientes según sus signos básicos.

## Construcción de la imagen

```bash
docker build -t prediccion-medica .

## Ejecuxión del Contenedor

docker run -d -p 5000:5000 prediccion-medica

## Uso del servicio

http://localhost:5000
