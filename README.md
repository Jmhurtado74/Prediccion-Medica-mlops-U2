# 🩺 Pipeline de MLOps – Reestructuración del Proyecto Médico

Este repositorio presenta la **propuesta final y reestructurada del pipeline MLOps** para el problema de predicción de enfermedades, incluidas enfermedades huérfanas, a partir de síntomas clínicos de un paciente.

La propuesta incluye:

- Diseño end-to-end del pipeline de Machine Learning.  
- Selección argumentada del stack tecnológico.  
- Suposiciones explícitas del sistema.  
- Diagrama profesional del pipeline.  
- Integración con prácticas de MLOps moderno (CI/CD, contenedores, despliegue, monitoreo, retraining).  
- CHANGELOG entre la propuesta inicial (Semana 1) y la propuesta final.

---

# 1. 📝 Introducción

El presente documento desarrolla una **reestructuración completa del pipeline de MLOps** aplicado al problema de predicción de enfermedades, incluyendo enfermedades huérfanas.  
Se revisa la propuesta inicial (Semana 1) y se formula una versión final:

- Robusta  
- Detallada  
- Reproducible  
- Alineada con buenas prácticas de ML y MLOps  

El objetivo es proveer una **guía integrable por un equipo de ML real**, explicando el pipeline end-to-end, tecnologías asociadas, suposiciones y decisiones de diseño.

---

# 2. 📘 Descripción del Problema

Los sistemas de información en salud almacenan grandes volúmenes de datos; sin embargo:

- Para **enfermedades frecuentes**, hay abundante información.  
- Para **enfermedades huérfanas**, los datos son escasos.

El modelo debe:

- Recibir síntomas clínicos como entrada.  
- Predecir probabilidad de enfermedad.  
- Diferenciar enfermedades comunes vs. huérfanas.  
- Funcionar localmente en el PC del médico **o** en la nube.  
- Mantener trazabilidad, calidad de datos y reproducibilidad.  
- Integrarse en un pipeline profesional MLOps.

**Objetivo:**  
Proponer un pipeline end-to-end completo, fundamentado y listo para desplegar.

---

# 3. 🏗️ Pipeline End-to-End Reestructurado de MLOps

El pipeline completo se organiza en **9 componentes principales**:

1. Ingesta y recolección de datos  
2. Procesamiento, limpieza y validación  
3. Entrenamiento y selección de modelos  
4. Evaluación, pruebas y explicabilidad  
5. Exportación del modelo a ONNX  
6. Contenerización con Docker  
7. Despliegue (local y en la nube)  
8. Monitoreo y observabilidad  
9. Retraining automático  

A continuación, cada componente se detalla.

---

## 3.1 📥 Ingesta y Recolección de Datos

### Fuentes de datos:
- Historias clínicas estructuradas  
- Registros de síntomas de médicos  
- Datasets pequeños de enfermedades huérfanas  
- Observaciones clínicas de sistema Web/App  

### Procesos realizados:
- Validación del tipo de dato  
- Normalización  
- Limpieza preliminar  
- Unificación de datasets  

### Tecnologías recomendadas:

| Tecnología | Justificación |
|-----------|--------------|
| AWS S3 / Azure Blob / GCP Storage | Almacenamiento seguro y escalable |
| Python + Pandas | Limpieza ligera |
| Apache Airflow | Orquestación automatizada |

---

## 3.2 🧹 Procesamiento y Limpieza de Datos

Incluye:

- Manejo de valores faltantes  
- Estandarización clínica  
- Normalización / escalado  
- Balanceo de clases (SMOTE)  
- Feature engineering  

### Tecnologías:
- Pandas  
- Scikit-Learn  
- Great Expectations (validación)  
- Airflow DAG (automatización)

---

## 3.3 🤖 División de Datos y Entrenamiento del Modelo

### Modelos candidatos:
- Random Forest  
- Gradient Boosting (XGBoost, LightGBM)  
- Redes neuronales ligeras  
- Modelos híbridos clínicos  

### Entrenamiento:
- Validación cruzada estratificada  
- Optimización de hiperparámetros (Optuna opcional)  
- Selección por macro-F1  

### Tecnologías:
- Scikit-Learn  
- XGBoost  
- MLflow Tracking  
- Optuna (tuning)

---

## 3.4 🧪 Validación, Pruebas y Explicabilidad

### Evaluación:
- F1-score macro  
- Curvas ROC  
- Precision-Recall  
- Matrices de confusión por tipo de enfermedad  

### Pruebas del pipeline:
- Pruebas unitarias con `pytest`  
- Tests de integración  

### Explicabilidad:
- SHAP para interpretación por clínicos  

---

## 3.5 📦 Exportación del Modelo (ONNX)

Ventajas del uso de ONNX:

- Alto rendimiento en inferencia  
- Arquitectura portable  
- Ejecución local o cloud  
- Runtime rápido (ONNX Runtime)

---

## 3.6 🐳 Contenerización con Docker

Docker permite:

- Reproducibilidad total  
- Empaquetar modelo + API  
- Ejecutar en cualquier entorno  
- Integración con CI/CD  

Tecnologías:

- Docker  
- Docker Compose (opcional)  
- GitHub Actions (validación automática)  

---

## 3.7 ☁️ Despliegue del Modelo

### **A. Despliegue Local (PC del médico)**
- Docker Desktop  
- API con Flask/FastAPI  
- ONNX Runtime  
- Ideal para áreas sin conectividad

### **B. Despliegue en la Nube**
Opciones:

| Servicio | Ventaja |
|---------|---------|
| AWS Lambda + API Gateway | Paga por uso, cero servidores |
| Google Cloud Run | Automatiza contenedores |
| Azure Functions | Integración Microsoft |
| EC2 / VMs | Control total |

---

## 3.8 📊 Monitoreo y Observabilidad

Aspectos monitoreados:

- Data drift  
- Concept drift  
- Latencia  
- Uso del sistema  

Tecnologías:

- Prometheus  
- Grafana  
- OpenTelemetry  
- MLflow Model Registry  

---

## 3.9 🔄 Retraining Automático

El sistema debe:

- Reentrenar con nuevos datos  
- Versionar modelos  
- Promover modelos de “staging → production”  
- Validar antes del despliegue  

Tecnologías:

- Apache Airflow  
- GitHub Actions  
- MLflow Registry  

---

# 4. 📐 Diagrama General del Pipeline

<div align="center">

<img src="https://github.com/user-attachments/assets/1c8c8ee8-4b4b-4596-a007-7ee4c83679b5" width="420">

</div>

---

# 5. 🛠️ Stack Tecnológico Justificado

| Etapa | Tecnología | Justificación |
|-------|------------|---------------|
| Ingesta | Airflow, Pandas | Orquestación, limpieza inicial |
| Limpieza | Sklearn, Great Expectations | Validación clínica |
| Entrenamiento | Sklearn/XGBoost, MLflow | Seguimiento robusto |
| Exportación | ONNX | Portabilidad |
| API | FastAPI/Flask | Despliegue rápido |
| Contenedores | Docker | Reproducibilidad |
| Cloud | Cloud Run, Lambda | Escalabilidad |
| CI/CD | GitHub Actions | Automatización |
| Monitoreo | Prometheus, Grafana | Observabilidad |
| Retraining | Airflow, Actions | Actualización continua |

---

# 6. 📄 Suposiciones Específicas

- Datos clínicos disponibles (estructurados).  
- Escasez de datos para enfermedades huérfanas.  
- Uso mayoritario en computadores con recursos moderados.  
- Soporte para despliegue híbrido (local + cloud).  
- Restricciones éticas y de privacidad.  
- Existencia de un equipo técnico mínimo (DE, DS, MLE).

---

# 7. 🧾 Conclusión

Este pipeline reestructurado presenta una arquitectura completa, moderna y profesional que cubre:

- Ciclo de vida del modelo  
- Calidad y validación de datos  
- Entrenamiento y evaluación  
- Contenerización  
- Despliegue local y cloud  
- Monitoreo real  
- Retraining automatizado  
- CI/CD integrado  

La propuesta final está **totalmente alineada con prácticas reales de MLOps**, asegurando reproducibilidad, escalabilidad y trazabilidad en entornos médicos, especialmente relevantes para enfermedades huérfanas.

