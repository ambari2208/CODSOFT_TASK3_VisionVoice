# VisionVoice – AI Image Captioning | CodSoft Internship Task 3

## About the Project

VisionVoice is an AI-powered image captioning web application that generates natural-language descriptions of uploaded images.

The project uses **Salesforce BLIP (Bootstrapping Language-Image Pre-training)**, a pre-trained vision-language model, to understand image content and convert it into meaningful captions.

I built this project to explore how computer vision and natural language processing can work together to make visual information easier to understand.

## Features

- **Image Upload:** Upload images using drag and drop or file selection.
- **Image Preview:** Preview the selected image before generating a caption.
- **AI Caption Generation:** Generate descriptions using the BLIP model.
- **Optional Starting Phrase:** Provide a phrase to guide caption generation.
- **Copy Caption:** Copy the generated description with one click.
- **Image Validation:** Supports JPG, JPEG, PNG, and WebP formats.
- **Upload Size Limit:** Accepts images up to 8 MB.
- **Responsive Interface:** A clean interface that adapts to different screen sizes.

## Technologies Used

- **Python** – Main programming language.
- **Flask** – Backend web framework.
- **Salesforce BLIP** – Pre-trained image captioning model.
- **PyTorch** – Deep learning framework.
- **Hugging Face Transformers** – Model and processor implementation.
- **Pillow** – Image processing and validation.
- **HTML, CSS and JavaScript** – Frontend development.

## Project Structure

```text
CODSOFT_TASK3_VisionVoice/
│
├── app.py
├── caption_service.py
├── image_utils.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── app.js
│   └── styles.css
│
├── templates/
│   └── index.html
│
└── tests/
    └── test_image_utils.py
```

## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/ambari2208/CODSOFT_TASK3_VisionVoice.git
```

**2. Navigate to the project folder**

```bash
cd CODSOFT_TASK3_VisionVoice
```

**3. Create a virtual environment**

```bash
python3 -m venv .venv
```

**4. Activate the virtual environment**

For macOS/Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

**5. Install the dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
python app.py
```

**7. Open the application**

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

*Note:* The BLIP model is loaded when the first caption is requested. Its model weights are downloaded from Hugging Face on the first run, so an internet connection is required. Subsequent requests can use the locally cached model.

## How It Works

1. The user uploads an image through the web interface.
2. Flask receives the image and passes it to the image validation utility.
3. The image is checked and converted into RGB format.
4. The BLIP processor prepares the image and optional starting phrase.
5. The pre-trained BLIP model analyses the image and generates a caption.
6. The generated description is returned to the frontend and displayed to the user.

## Running Tests

The project includes tests for image validation and image processing.

Run them using:

```bash
python -m unittest discover -s tests -v
```

These tests check valid image processing and handling of unsupported or invalid image files without requiring the BLIP model to download.

## What I Learned

Through this project, I explored:

- How pre-trained vision-language models work.
- How computer vision connects with natural language processing.
- How to integrate a Hugging Face model into a Flask application.
- How to handle image uploads and validate input files.
- How to connect a Python backend with a JavaScript frontend.

---

**CodSoft AI Internship – Task 3**

*Image Captioning AI | VisionVoice*
