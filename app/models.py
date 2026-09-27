from app import db

# TODO(Member C): flesh out these models and run migrations against RDS.


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class FileRecord(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    s3_key = db.Column(db.String(512), nullable=False)
    category = db.Column(db.String(100))
    size_bytes = db.Column(db.Integer)
    content_type = db.Column(db.String(100))
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())
