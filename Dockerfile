FROM python:3.9-slim

LABEL maintainer="Juan Manuel Hurtado Angulo & Manuel Alberto González González"
LABEL description="Aplicación Flask para diagnóstico médico simulado - Proyecto MLOps"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
