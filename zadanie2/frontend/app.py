import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    try:
        response = requests.get("http://backend:9000/api/data")
        data = response.json()
        message = data.get("data", "No data")
    except requests.exceptions.ConnectionError:
        message = "Could not connect to backend API."

    return f"<h1>Frontend App</h1><p>{message}</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)