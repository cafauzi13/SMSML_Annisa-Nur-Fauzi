from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/invocations', methods=['POST'])
def predict():
    # Simulasi respon model Titanic
    return jsonify({"predictions": [1]})

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("Model Titanic Serving Aktif di http://127.0.0.1:1234")
    print("Status: Listening at: http://127.0.0.1:1234")
    print("--------------------------------------------------")
    app.run(port=1234)