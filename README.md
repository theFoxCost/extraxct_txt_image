# 📌 Python OCR Script with Pytesseract

## 🚀 Description
This project extracts text from images using Python's `PIL` (Pillow) and `pytesseract` libraries.

## 🔧 Features
- 📸 Supports image input (default: `thumbnail.png`)
- 🔍 Converts image content to text
- ✅ Lightweight and easy to customize

## 📦 Requirements
Ensure you have the following installed:
- Python 3.12+
- `pytesseract`
- `Pillow`
- Tesseract-OCR (installed in the system)

### 🛠️ Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install dependencies:
    ```bash
    pip install Pillow pytesseract
    ```

3. Ensure Tesseract-OCR is installed:
    ```bash
    sudo apt-get install tesseract-ocr -y
    ```

## 🔥 Usage
Run the script:
```bash
python script.py
```

It’ll prompt for an image filename. If left blank, it defaults to `thumbnail.png`.

## 🛠️ Docker Support
If you’re running this in Docker:
```bash
docker build -t ocr-script .
docker run -it ocr-script
```

## 🛠️ Contributing
Feel free to fork this project, make improvements, and submit pull requests!

## 📄 License
This project is open-source under the MIT License.

---

Made with 💻 and ☕ by [theFoxCost](https://github.com/theFoxCost)
