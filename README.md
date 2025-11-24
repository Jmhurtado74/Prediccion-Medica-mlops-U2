Pipeline de MLOps – Reestructuración del Proyecto Médico 
Este repositorio presenta la propuesta final y reestructurada del pipeline MLOps para el problema de predicción de enfermedades incluidas enfermedades huérfanas a partir de síntomas clínicos de un paciente.
La propuesta incluye:
•	Diseño end-to-end del pipeline de Machine Learning,
•	Selección argumentada del stack tecnológico,
•	Suposiciones explícitas del sistema,
•	 	Diagrama moderno genera grandes cantidades de datos. Sin embargo, para enfermedades huérfanas (poco comunes), la cantidad de datos es escasa. Se requiere un sistema de predicción profesional del pipeline,
•	Integración con MLOps moderno (CI/CD, contenedores, despliegue, monitoreo, retraining),
•	CHANGELOG entre la propuesta inicial (Semana 1) y esta propuesta final.
1. Introducción
El presente documento desarrolla una propuesta de reestructuración completa del pipeline de MLOps aplicado al problema de predicción de enfermedades, incluyendo enfermedades huérfanas, a partir de datos clínicos de pacientes. A la luz de los contenidos trabajados en el curso, se revisa la propuesta inicial planteada en la primera semana y se formula una versión final, robusta y alineada con buenas prácticas de ingeniería de datos, ciencia de datos y MLOps.
La propuesta se concibe como una guía suficientemente detallada para que un equipo de aprendizaje automático pueda implementarla sin ambigüedades. Para ello se describen las etapas del pipeline end-to-end, las tecnologías recomendadas, las suposiciones realizadas y los cambios más relevantes frente a la versión inicial.

 1. Descripción del Problema
El problema a abordar se resume así: los sistemas de información en salud almacenan grandes volúmenes de datos de pacientes, pero la distribución de dichos datos es desigual. Para enfermedades frecuentes existe abundante información histórica, mientras que para enfermedades huérfanas o poco comunes la disponibilidad de datos es limitada.
Se requiere construir un modelo que, a partir de los síntomas y características clínicas de un paciente, permita predecir si es posible o no que presente cierto tipo de enfermedad. La solución debe ser útil tanto para enfermedades comunes como para enfermedades huérfanas y debe poder ser consumida por personal médico desde su computador local o mediante servicios desplegados en la nube.

La medicina capaz de:
•	Diferenciar entre enfermedades comunes y huérfanas.
•	Recibir síntomas clínicos como entrada.
•	Entregar una predicción confiable al médico.
•	Permitir ejecución local (en el PC del médico) o remota (en la nube).
•	Mantener trazabilidad, calidad de datos, reproducibilidad del modelo y despliegues automatizados.
El objetivo es definir un pipeline profesional de MLOps, totalmente reestructurado, que cubra el ciclo de vida completo del modelo, desde los datos hasta la operación y mantenimiento.

 2. Pipeline End-to-End Reestructurado de MLOps
La propuesta final plantea un pipeline end-to-end que cubre todo el ciclo de vida del modelo: ingesta, limpieza y validación de datos, entrenamiento y evaluación, empaquetado y despliegue, monitoreo en producción y retraining periódico.
En términos generales, el flujo se organiza en nueve grandes componentes:
1.	Ingesta y almacenamiento de datos.
2.	Procesamiento, limpieza y validación de calidad.
3.	Entrenamiento y selección de modelos.
4.	Evaluación, pruebas y explicabilidad.
5.	Exportación del modelo a un formato portable (ONNX).
6.	Contenerización con Docker.
7.	Despliegue local y en la nube.
8.	Monitoreo y observabilidad.
9.	Retraining y gestión del ciclo de vida del modelo.
A continuación se describe cada componente con mayor detalle.

 2.1 Ingesta y Recolección de Datos
Fuentes de datos:
•	Historias clínicas estructuradas.
•	Registros de síntomas ingresados por médicos.
•	Datos de enfermedades huérfanas (datasets pequeños).
•	Observaciones clínicas provenientes del sistema web/App.
Procesos:
•	Validación del tipo de dato.
•	Normalización y limpieza preliminar.
•	Control de calidad inicial.
•	Unificación de fuentes heterogéneas.
Tecnologías recomendadas:
Tecnología	Justificación
AWS S3 / Azure Blob / GCP Storage	Almacenamiento duradero, seguro y escalable.
Python + Pandas	Transformaciones ligeras y flexibles.
Apache Airflow	Orquestación de pipelines para ingesta periódica.

2.2 Procesamiento y Limpieza de Datos
Incluye:
•	Manejo y tratamiento de valores faltantes.
•	Estandarización clínica (rangos seguros, unidades).
•	Normalización / Escalamiento.
•	Balanceo de clases (SMOTE para enfermedades huérfanas).
•	Feature engineering clínico.
Tecnologías recomendadas:
•	Pandas para manipulación.
•	Scikit-Learn para normalización y features.
•	Great Expectations para pruebas de calidad de datos.
•	Airflow DAG automatizando estos pasos.

 2.3 División de Datos y Entrenamiento del Modelo
El modelo debe:
•	Aprender de datasets balanceados.
•	Funcionar en contextos de alta y baja disponibilidad de datos.
•	Generalizar bien a enfermedades raras.
Modelos candidatos:
•	Random Forest
•	Gradient Boosting (XGBoost / LightGBM)
•	Redes neuronales ligeras
•	Modelos híbridos basados en reglas + ML
Entrenamiento:
•	Validación cruzada estratificada.
•	Optimización de hiperparámetros (Optuna opcional).
•	Selección basada en métricas balanceadas (macro-F1).
Tecnologías:
•	Scikit-Learn / XGBoost
•	MLflow Tracking para registro de experimentos.
•	Optuna para tuning.

 2.4 Validación del Modelo
•	Métricas usadas: F1-score, ROC, Precision-Recall.
•	Curvas comparativas entre modelos.
•	Pruebas unitarias de comportamiento e integración con pytest.
•	Explicabilidad con SHAP (para médicos).
Tecnologías:
•	MLflow para versionar resultados.
•	SHAP para interpretabilidad.
•	pytest para pruebas unitarias del pipeline.

 2.5 Exportación del Modelo (ONNX)
El modelo entrenado se convierte a ONNX, lo que permite:
•	Ejecución rápida.
•	Tamaño reducido.
•	Inferencia portable entre nubes, PC local, móviles, servicios web.
•	Optimización del tiempo de predicción.
Tecnologías:
•	ONNX
•	ONNX Runtime

 2.6 Empaquetado con Docker
El modelo + API se empaquetan en una imagen Docker:
Ventajas:
•	Reproducibilidad total.
•	Mismo entorno para desarrollo, pruebas y producción.
•	Fácil despliegue en cloud o local.
Tecnologías:
•	Docker
•	Docker Compose (opcional para varios contenedores)
•	GitHub Actions para validación automática

2.7 Despliegue del Modelo
 “El médico puede correr el modelo localmente o desde la nube”. Por eso se definen dos rutas de despliegue:
A. Despliegue Local (en el PC del médico)
•	API Flask/FastAPI levantada con Docker Desktop.
•	ONNX Runtime para predicción rápida.
•	Ideal para zonas remotas o sin internet.

B. Despliegue en la Nube
Opciones:
Servicio	Ventaja
AWS Lambda + API Gateway	Paga por uso, cero mantenimiento, ideal para APIs ML pequeñas.
Google Cloud Run	Despliegue automático de contenedores.
Azure Functions	Integración con herramientas Microsoft.
EC2 / VM con Docker	Mayor control, útil para hospitales.

2.8 Monitoreo y Observabilidad
Aspectos monitoreados:
•	Cambios en la distribución de datos (data drift).
•	Cambios en el rendimiento (concept drift).
•	Latencia de predicciones.
•	Uso y carga del sistema.
Tecnologías:
•	Prometheus + Grafana
•	OpenTelemetry
•	MLflow Model Registry

2.9 Retraining Automático
El sistema debe:
•	Reentrenar usando nuevos datos clínicos.
•	Guardar versiones nuevas del modelo.
•	Validar antes de publicar.
Tecnologías:
•	Apache Airflow para DAG de retraining.
•	GitHub Actions para disparar reentrenamientos programados.
•	MLflow Registry para promover modelos (“staging → production”).

 3. Diagrama General del Pipeline MLOps
Incluye todo el ciclo de vida:
 

4. Stack Tecnológico Justificado
Etapa	Tecnología	Justificación
Ingesta	Airflow, Pandas	Orquestación y limpieza inicial
Limpieza/Transformación	Sklearn, Great Expectations	Estandarización y validación de datos
Entrenamiento	Sklearn/XGBoost, MLflow	Seguimiento de experimentos
Exportación	ONNX	Portabilidad y velocidad
API	FastAPI/Flask	Bajo acoplamiento, fácil despliegue
Contenedores	Docker	Reproducibilidad
Cloud	Cloud Run / Lambda	Escalabilidad
CI/CD	GitHub Actions	Automatización del flujo
Monitoreo	Grafana/Prometheus	Observabilidad
Retraining	Airflow/Actions	Actualización periódica

 5. Suposiciones Específicas
Dada la naturaleza abierta del problema, se establecen las siguientes suposiciones explícitas:
•	Se dispone de un conjunto de datos clínicos históricos con variables demográficas, signos vitales, síntomas, diagnósticos y etiquetas de presencia o ausencia de enfermedad.
•	Para enfermedades huérfanas existe menos información, por lo que se requerirán estrategias de balanceo de clases y técnicas robustas ante el desbalance.
•	El uso final del modelo será principalmente por médicos generales o especialistas que, en algunos casos, solo cuentan con un equipo de cómputo de recursos moderados, sin GPU dedicada.
•	La institución de salud dispone de algún proveedor de nube (por ejemplo, AWS, Azure o GCP) para montar servicios de inferencia y almacenamiento seguro de datos.
•	Existen lineamientos éticos y de protección de datos que restringen el acceso directo a información identificable de los pacientes; el pipeline debe registrar métricas agregadas y no datos sensibles.
•	Se cuenta con un equipo mínimo de datos y ML (data engineer, data scientist, ML engineer) responsable de operar, monitorear y evolucionar el sistema.
Estas suposiciones permiten delimitar el alcance de la solución y orientan las decisiones técnicas.


6. Conclusión
Esta propuesta reestructurada presenta un pipeline MLOps completo, robusto y profesional que cubre Ciclo de vida del modelo, Calidad de datos, Entrenamiento y validación, Contenerización, Despliegue local y cloud, Monitoreo y retraining, Integración continua.
La reestructuración del pipeline de MLOps propuesta en este documento transforma una idea general de modelado en un proceso end-to-end claramente definido, tecnológicamente viable y alineado con prácticas profesionales.
La integración de herramientas como Airflow, MLflow, ONNX, Docker y GitHub Actions permite garantizar reproducibilidad, escalabilidad y trazabilidad. Asimismo, la consideración de mecanismos de monitoreo y reentrenamiento continuo resulta fundamental para mantener la utilidad clínica del modelo en el tiempo, especialmente en el contexto de enfermedades huérfanas donde los datos evolucionan y se incrementan de forma paulatina.
Con esta propuesta, un equipo de ML cuenta con una hoja de ruta detallada para implementar, desplegar y mantener un sistema de predicción médica robusto, cumpliendo los criterios de calificación del curso y alineándose con los desafíos reales de la práctica profesional en MLOps.
