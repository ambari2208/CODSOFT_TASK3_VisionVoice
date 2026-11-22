"""Tests for upload validation that do not require downloading the AI model."""

from io import BytesIO
import unittest

from PIL import Image

from image_utils import ImageValidationError, read_uploaded_image


class FakeUpload:
    def __init__(self, filename: str, data: bytes):
        self.filename = filename
        self._data = data

    def read(self) -> bytes:
        return self._data


def png_bytes() -> bytes:
    image = Image.new("RGB", (3, 2), color=(45, 120, 220))
    stream = BytesIO()
    image.save(stream, format="PNG")
    return stream.getvalue()


class ImageUtilsTests(unittest.TestCase):
    def test_valid_png_becomes_rgb_image(self) -> None:
        image = read_uploaded_image(FakeUpload("sample.png", png_bytes()))
        self.assertEqual(image.mode, "RGB")
        self.assertEqual(image.size, (3, 2))

    def test_rejects_unsupported_extension(self) -> None:
        with self.assertRaisesRegex(ImageValidationError, "image types"):
            read_uploaded_image(FakeUpload("sample.gif", b"not-used"))

    def test_rejects_corrupt_image(self) -> None:
        with self.assertRaisesRegex(ImageValidationError, "not a valid image"):
            read_uploaded_image(FakeUpload("sample.jpg", b"not-an-image"))


if __name__ == "__main__":
    unittest.main()
