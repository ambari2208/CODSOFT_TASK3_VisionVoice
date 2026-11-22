"""Lazy-loading image captioning service powered by a BLIP model."""

from __future__ import annotations

from threading import Lock


class ModelLoadError(RuntimeError):
    """Raised when the captioning model cannot be loaded."""


class CaptionService:
    """Generate image captions with Salesforce's BLIP image-captioning model.

    The model is loaded only for the first caption request. This lets the web
    interface open immediately and avoids downloading model weights at import
    time.
    """

    MODEL_ID = "Salesforce/blip-image-captioning-base"

    def __init__(self) -> None:
        self._processor = None
        self._model = None
        self._torch = None
        self._load_lock = Lock()

    def _load_model(self) -> None:
        if self._model is not None:
            return

        with self._load_lock:
            if self._model is not None:
                return
            try:
                import torch
                from transformers import BlipForConditionalGeneration, BlipProcessor

                self._processor = BlipProcessor.from_pretrained(self.MODEL_ID)
                self._model = BlipForConditionalGeneration.from_pretrained(self.MODEL_ID)
                self._model.eval()
                self._torch = torch
            except Exception as error:
                raise ModelLoadError(
                    "The BLIP model could not be loaded. Check your internet connection "
                    "for the first run and confirm the project dependencies are installed."
                ) from error

    def caption(self, image, prompt: str = "") -> str:
        """Return a short natural-language caption for a Pillow image."""
        self._load_model()
        inputs = self._processor(images=image, text=prompt or None, return_tensors="pt")

        with self._torch.no_grad():
            output_ids = self._model.generate(
                **inputs,
                max_new_tokens=40,
                num_beams=4,
            )

        caption = self._processor.decode(output_ids[0], skip_special_tokens=True).strip()
        if not caption:
            raise RuntimeError("The model returned an empty caption.")
        return caption[0].upper() + caption[1:]
