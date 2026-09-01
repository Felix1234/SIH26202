import os

from flask import Blueprint, request, jsonify

from services.analysis_service import analyze_file


upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = "datasets/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@upload_bp.route("/upload", methods=["POST"])
def upload_file():

    # Check whether a file was uploaded
    if "file" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file uploaded"
        }), 400

    file = request.files["file"]

    # Check whether a file was selected
    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected"
        }), 400

    filename = file.filename

    # Get file extension
    extension = filename.rsplit(".", 1)[-1].lower()

    # Allowed file types
    allowed_extensions = [
        "csv",
        "xlsx",
        "xls",
        "pdf"
    ]

    if extension not in allowed_extensions:
        return jsonify({
            "success": False,
            "message": "Unsupported file type"
        }), 400

    # Save the uploaded file
    file_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(file_path)

    try:

        # Analyze the uploaded file
        result = analyze_file(
            file_path,
            extension
        )

        return jsonify({
            "success": True,
            "filename": filename,
            "result": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500