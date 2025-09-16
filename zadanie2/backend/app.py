from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify({"data": "Data from backend API"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)