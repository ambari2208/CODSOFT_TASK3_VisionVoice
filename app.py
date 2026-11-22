"""Flask application for the CodSoft image-captioning project."""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge

from caption_service import CaptionService, ModelLoadError
from image_utils import ImageValidationError, read_uploaded_image


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8 MB upload limit
    app.caption_service = CaptionService()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/api/caption")
    def generate_caption():
        upload = request.files.get("image")
        prompt = request.form.get("prompt", "").strip()

        try:
            image = read_uploaded_image(upload)
            caption = app.caption_service.caption(image, prompt=prompt)
        except ImageValidationError as error:
            return jsonify({"error": str(error)}), 400
        except ModelLoadError as error:
            return jsonify({"error": str(error)}), 503
        except Exception:
            app.logger.exception("Caption generation failed")
            return jsonify({"error": "Caption generation failed. Please try another image."}), 500

        return jsonify({"caption": caption})

    @app.errorhandler(RequestEntityTooLarge)
    def handle_large_upload(_error):
        return jsonify({"error": "The image is too large. Please choose a file under 8 MB."}), 413

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
