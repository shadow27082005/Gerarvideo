from flask import Flask
from lib.backend.routes.gerar_video import video_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(video_bp, url_prefix='/api')
    return app

