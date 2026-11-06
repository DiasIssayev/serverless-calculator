from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Calculator server is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}

    for key in ("a", "b", "operation"):
        if key not in data:
            return jsonify({"error": f"Отсутствует параметр '{key}'"}), 400

    a = data["a"]
    b = data["b"]
    operation = data["operation"]

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "Деление на ноль невозможно"}), 400
        result = a / b
    else:
        return jsonify({"error": f"Неизвестная операция: {operation}"}), 400

    return jsonify({"result": result})
