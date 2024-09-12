from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Habilitar CORS para permitir que Angular se comunique con Flask
    CORS(app)  # Esto aplica CORS a todas las rutas
    
    # Registrar las rutas
    from .routes import main  # Asegúrate de que este nombre es correcto y apunta al archivo de rutas
    app.register_blueprint(main)
    
    return app
