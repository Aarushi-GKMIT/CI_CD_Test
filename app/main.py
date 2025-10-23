from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask CI/CD Demo!"

@app.route('/square', methods=['POST'])
def square():
    data = request.get_json()
    if not data or 'number' not in data:
        return jsonify({"error": "Please provide a number"}), 400
    try:
        num = float(data['number'])
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400
    return jsonify({"number": num, "square": num**2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
