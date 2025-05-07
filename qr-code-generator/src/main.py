# filepath: qr-code-generator/src/main.py

from flask import Flask, request, jsonify
from user_management import UserManager
from qr_generator import QRCodeGenerator

app = Flask(__name__)
user_manager = UserManager()
qr_generator = QRCodeGenerator()

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if user_manager.add_user(username, password):
        return jsonify({"message": "User registered successfully."}), 201
    return jsonify({"message": "User already exists."}), 400

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if user_manager.authenticate_user(username, password):
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid credentials."}), 401

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    qr_data = data.get('data')
    file_path = data.get('file_path')
    if qr_data and file_path:
        qr_generator.generate_qr_code(qr_data)
        qr_generator.save_qr_code(file_path)
        return jsonify({"message": "QR code generated successfully."}), 200
    return jsonify({"message": "Invalid data."}), 400

@app.route('/users', methods=['GET'])
def list_users():
    users = user_manager.list_users()
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)