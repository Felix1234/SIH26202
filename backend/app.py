from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.upload_routes import upload_bp
import os


app = Flask(__name__)

CORS(app)

app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024


# =========================
# API
# =========================

app.register_blueprint(
    upload_bp,
    url_prefix="/api"
)


# =========================
# FRONTEND PATH
# =========================

FRONTEND_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../frontend"
    )
)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():

    return send_from_directory(
        os.path.join(
            FRONTEND_FOLDER,
            "html"
        ),
        "index.html"
    )


# =========================
# CSS FILES
# =========================

@app.route("/css/<path:filename>")
def css_files(filename):

    return send_from_directory(
        os.path.join(
            FRONTEND_FOLDER,
            "css"
        ),
        filename
    )


# =========================
# JAVASCRIPT FILES
# =========================

@app.route("/js/<path:filename>")
def js_files(filename):

    return send_from_directory(
        os.path.join(
            FRONTEND_FOLDER,
            "js"
        ),
        filename
    )


# =========================
# HEALTH CHECK
# =========================

@app.route("/health")
def health():

    return {
        "status": "OK"
    }


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    app.run(
        debug=False,
        host="127.0.0.1",
        port=5000
    )
