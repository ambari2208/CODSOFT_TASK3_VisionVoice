"""Validation helpers for user-uploaded images."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

from PIL import Image, UnidentifiedImageError


class ImageValidationError(ValueError):
    """Raised when an upload is missing or cannot be processed as an image."""


ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def read_uploaded_image(upload) -> Image.Image:
    """Validate a Flask FileStorage object and return an RGB Pillow image."""
    if upload is None or not upload.filename:
        raise ImageValidationError("Choose an image before generating a caption.")

    suffix = Path(upload.filename).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        allowed = ", ".join(sorted(ALLOWED_EXTENSIONS))
        raise ImageValidationError(f"Use one of these image types: {allowed}.")

    data = upload.read()
    if not data:
        raise ImageValidationError("The selected image is empty.")

    try:
        with Image.open(BytesIO(data)) as candidate:
            candidate.verify()
        with Image.open(BytesIO(data)) as candidate:
            return candidate.convert("RGB")
    except (UnidentifiedImageError, OSError, ValueError) as error:
        raise ImageValidationError("This file is not a valid image.") from error
