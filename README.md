# CODSOFT_TASK3 - VisionVoice Image Captioning AI

VisionVoice is a polished web application that generates natural-language descriptions of uploaded images. It uses **Salesforce BLIP**, a pre-trained vision-language transformer, to connect computer vision with natural-language processing.

## What it demonstrates

- Computer vision: BLIP's image encoder extracts meaningful visual features.
- Natural-language processing: the language decoder turns those features into a fluent caption.
- Pre-trained transformer inference: the project uses `Salesforce/blip-image-captioning-base` through Hugging Face Transformers.
- Responsive user interface: users can drag and drop or select an image, preview it, guide the caption with an optional phrase, and copy the result.

## Project structure

```text
CODSOFT_TASK3/
|- app.py                  # Flask routes and API
|- caption_service.py      # Lazy-loaded BLIP inference service
|- image_utils.py          # Safe image validation
|- requirements.txt        # Python dependencies
|- static/                 # Browser interface assets
|- templates/              # Flask HTML template
`- tests/                  # Validation tests
```

## Run locally

1. Open a terminal in this project folder.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Visit `http://127.0.0.1:5000` in your browser.

On the first caption request, Transformers downloads the BLIP model weights and stores them in its local cache. This may take several minutes and requires an internet connection only once. Later requests use the cached model.

## Run tests

```bash
python -m unittest discover -s tests -v
```

These tests validate successful image processing and invalid-upload handling without downloading the AI model.

## How caption generation works

1. The browser sends the selected image to `/api/caption`.
2. The server validates the file type and decodes it safely with Pillow.
3. `CaptionService` loads the pre-trained BLIP processor and model on the first request.
4. BLIP encodes visual features, then generates a caption with beam search.
5. The caption is returned to the interface and displayed for the user.

## Suggested video demo

1. Introduce the VisionVoice interface and its upload panel.
2. Upload a clear image containing multiple recognizable objects.
3. Click **Generate caption** and show the loading state.
4. Read the generated caption and use **Copy caption**.
5. Explain that BLIP combines an image encoder with a transformer language decoder.
6. Briefly show `caption_service.py` and point out the `caption()` method.
