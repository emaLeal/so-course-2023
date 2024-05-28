from flask import Flask, request, send_from_directory, jsonify
import os, shutil

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
    return send_from_directory(public_dir, name, as_attachment=True)

@app.route('/upload/<uid>/<name>', methods=['POST'])
def upload_file(uid, name):
     # Definir las rutas de las carpetas public y private
    carpeta_public = f"{BASE_DIR}/public"
    carpeta_private = f"{BASE_DIR}/private/{uid}"
    
    # Construir las rutas completas del archivo de origen y destino
    ruta_origen = os.path.join(carpeta_public, name)
    ruta_destino = os.path.join(carpeta_private, name)
    try:
        shutil.move(ruta_origen, ruta_destino)
        print(f"Archivo {name} movido de {carpeta_public} a {carpeta_private}")
        return jsonify({"message": "File uploaded successfully"}), 201
    except FileNotFoundError:
        print(f"Archivo {name} no encontrado en {carpeta_public}")
        return jsonify({"message": "Error"}), 500

    except Exception as e:
        print(f"Ocurrió un error al mover el archivo: {e}")
        return jsonify({"message": "Error"}), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)