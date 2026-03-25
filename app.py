from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os

# Lädt die Variablen aus der `.env`-Datei
load_dotenv()

app = Flask(__name__)


# Datenbankkonfiguration aus Umgebungsvariablen
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB_Clima')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisieren der Datenbank
db = SQLAlchemy(app)

# Modell für die "climate_data"-Tabelle
class ClimateData(db.Model):
    __tablename__ = 'climate_data'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255), nullable=False)

# Endpunkt, um alle Daten abzurufen
@app.route('/data', methods=['GET'])
def get_data():
    data = ClimateData.query.all()
    result = [{"id": d.id, "temperature": d.temperature, "humidity": d.humidity, "timestamp": d.timestamp, "location": d.location} for d in data]
    return jsonify(result)

# Endpunkt, um einen neuen Datensatz hinzuzufügen
@app.route('/addData', methods=['POST'])
def add_data():
    data = request.get_json()

    time = datetime.now()
    
    # Validierung der Eingabedaten
    if not all(k in data for k in ["temperature", "humidity", "location"]):
        return jsonify({"error": "Missing fields"}), 400

    new_data = ClimateData(
        temperature=data["temperature"],
        humidity=data["humidity"],
        timestamp=time,
        location=data["location"]
    )

    db.session.add(new_data)
    db.session.commit()

    return jsonify({"message": "Data added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
