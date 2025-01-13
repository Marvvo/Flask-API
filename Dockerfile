# Verwende ein Python-Image
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Inhalt der aktuellen Verzeichnisses ins Container
COPY . .

# Setze die Umgebungsvariable für Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Öffne den Flask-Standardport
EXPOSE 5000

# Starten der Flask-Anwendung
CMD ["python", "app.py"]
