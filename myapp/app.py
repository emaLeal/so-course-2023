from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)
BASE_DIR = "/sync_files"

@app.route('/')
def hello_world():
  return {
    'message': 'hola, Mundo!!!'
  }

@app.route('/despedirse')
def bye_world():
  return {
    'message': 'Adiós, mundo!!!'
  }

@app.route('/storage/<uid>', methods=['GET'])
def list_files(uid):
    user_dir = os.path.join(BASE_DIR, 'private', uid)
    if not os.path.exists(user_dir):
        return jsonify({"error": "User directory not found"}), 404
    files = os.listdir(user_dir)
    return jsonify(files)

@app.route('/public/', methods=['GET'])
def list_public_files():
    public_dir = os.path.join(BASE_DIR, 'public')
    files = os.listdir(public_dir)
    return jsonify(files)

@app.route('/download/<name>', methods=['GET'])
def download_file(name):
    public_dir = os.path.join(BASE_DIR, 'public')
    return send_from_directory(public_dir, name)

@app.route('/upload/<uid>/<name>', methods=['POST'])
def upload_file(uid, name):
    user_dir = os.path.join(BASE_DIR, 'private', uid)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    file = request.files['file']
    file.save(os.path.join(user_dir, name))
    return jsonify({"message": "File uploaded successfully"}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)