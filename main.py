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
            return jsonify({
                "message": f"Ошибка: отсутствует параметр '{key}'"
            })

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
            return jsonify({
                "message": "Нельзя делить на ноль!"
            })
        result = a / b

    else:
        return jsonify({
            "message": f"Неизвестная операция: {operation}"
        })

    return jsonify({"result": result})
