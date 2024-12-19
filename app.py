from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api', methods=['GET'])
def hello_world():
    """
    Eine einfache API, die "OK" zurückgibt.
    ---
    responses:
      200:
        description: Eine OK-Antwort
    """
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
