import os
from dotenv import load_dotenv

load_dotenv()

_db_url = os.environ.get("DATABASE_URL")
if _db_url and _db_url.startswith("postgresql://"):
    _db_url = _db_url.replace("postgresql://", "postgresql+psycopg2://", 1)


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
    AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
    SHARE_LINK_EXPIRY_MINUTES = int(os.environ.get("SHARE_LINK_EXPIRY_MINUTES", 60))
