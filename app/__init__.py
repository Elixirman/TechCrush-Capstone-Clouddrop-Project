from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"error": "login required"}), 401

    from .auth import auth_bp
    from .upload import upload_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(upload_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app