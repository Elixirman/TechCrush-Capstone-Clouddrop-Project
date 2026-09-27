from flask import Blueprint, jsonify, request
import boto3
from .config import Config

upload_bp = Blueprint("upload", __name__, url_prefix="/files")

s3_client = boto3.client("s3", region_name=Config.AWS_REGION)

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "docx", "txt", "csv"}
MAX_FILE_SIZE_MB = 25


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# TODO(Member B): implement real upload.
# - Validate file type (use allowed_file) and size (MAX_FILE_SIZE_MB)
# - Upload to S3 using s3_client.upload_fileobj(file, Config.S3_BUCKET_NAME, key)
# - Save a FileRecord row (from models.py) with the S3 key + metadata
@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    return jsonify({"message": "TODO: implement upload"}), 501


# TODO(Member B): implement real download.
# - Look up the FileRecord by id, confirm the requester owns it
# - Stream the file back from S3 or return a presigned URL
@upload_bp.route("/<int:file_id>/download", methods=["GET"])
def download_file(file_id):
    return jsonify({"message": f"TODO: implement download for file {file_id}"}), 501


# TODO(Member D): implement temporary sharing links.
# - Use s3_client.generate_presigned_url("get_object", Params={...}, ExpiresIn=...)
# - Expiry should come from Config.SHARE_LINK_EXPIRY_MINUTES
@upload_bp.route("/<int:file_id>/share", methods=["POST"])
def share_file(file_id):
    return jsonify({"message": f"TODO: implement share link for file {file_id}"}), 501


# TODO(Member B): implement search/filter by category, filename, date.
@upload_bp.route("/search", methods=["GET"])
def search_files():
    query = request.args.get("q", "")
    return jsonify({"message": "TODO: implement search", "query": query}), 501
