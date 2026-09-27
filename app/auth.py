from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# TODO(Member C): implement real registration.
# - Hash passwords (use werkzeug.security.generate_password_hash)
# - Save the user to the database via a User model in models.py
# - Validate that email/username isn't already taken
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    return jsonify({"message": "TODO: implement registration", "received": data}), 501


# TODO(Member C): implement real login.
# - Look up the user, verify password hash
# - Issue a session (flask-login) or JWT
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    return jsonify({"message": "TODO: implement login", "received": data}), 501
