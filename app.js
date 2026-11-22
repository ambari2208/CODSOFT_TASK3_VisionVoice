const imageInput = document.querySelector("#image-input");
const dropzone = document.querySelector("#dropzone");
const preview = document.querySelector("#preview");
const dropzoneEmpty = document.querySelector("#dropzone-empty");
const fileName = document.querySelector("#file-name");
const promptInput = document.querySelector("#prompt");
const generateButton = document.querySelector("#generate-button");
const resultEmpty = document.querySelector("#result-empty");
const loading = document.querySelector("#loading");
const captionResult = document.querySelector("#caption-result");
const captionText = document.querySelector("#caption-text");
const errorMessage = document.querySelector("#error-message");
const copyButton = document.querySelector("#copy-button");

let selectedFile = null;
let previewUrl = null;

function showImage(file) {
  if (!file || !file.type.startsWith("image/")) {
    showError("Please select a JPG, PNG, or WebP image.");
    return;
  }
  if (previewUrl) URL.revokeObjectURL(previewUrl);
  selectedFile = file;
  previewUrl = URL.createObjectURL(file);
  preview.src = previewUrl;
  preview.hidden = false;
  dropzoneEmpty.hidden = true;
  fileName.textContent = file.name;
  generateButton.disabled = false;
  hideError();
}

function showError(message) {
  errorMessage.textContent = message;
  errorMessage.hidden = false;
}

function hideError() {
  errorMessage.hidden = true;
  errorMessage.textContent = "";
}

function setResultState(state) {
  resultEmpty.hidden = state !== "empty";
  loading.hidden = state !== "loading";
  captionResult.hidden = state !== "caption";
}

imageInput.addEventListener("change", () => showImage(imageInput.files[0]));

["dragenter", "dragover"].forEach((eventName) => {
  dropzone.addEventListener(eventName, (event) => {
    event.preventDefault();
    dropzone.classList.add("is-dragging");
  });
});

["dragleave", "drop"].forEach((eventName) => {
  dropzone.addEventListener(eventName, (event) => {
    event.preventDefault();
    dropzone.classList.remove("is-dragging");
  });
});

dropzone.addEventListener("drop", (event) => showImage(event.dataTransfer.files[0]));

generateButton.addEventListener("click", async () => {
  if (!selectedFile) return;
  hideError();
  setResultState("loading");
  generateButton.disabled = true;

  const formData = new FormData();
  formData.append("image", selectedFile);
  formData.append("prompt", promptInput.value.trim());

  try {
    const response = await fetch("/api/caption", { method: "POST", body: formData });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Unable to create a caption.");
    captionText.textContent = data.caption;
    setResultState("caption");
  } catch (error) {
    setResultState("empty");
    showError(error.message || "Unable to create a caption.");
  } finally {
    generateButton.disabled = false;
  }
});

copyButton.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(captionText.textContent);
    copyButton.textContent = "Copied!";
    window.setTimeout(() => { copyButton.textContent = "Copy caption"; }, 1300);
  } catch {
    showError("Unable to copy automatically. Please select the caption manually.");
  }
});
