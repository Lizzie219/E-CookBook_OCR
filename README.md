# E-CookBook_OCR

This is the OCR server of the E-CookBook web application.

The included container runs on Cloud Run's `PORT` (8080 by default) with
Gunicorn. Build the image with this directory as the Docker build context.

Tesseract OCR for python (pytesseract) is needed for this to work, change the 'path of pytesseract' part of the code accordingly.

Pytesseract can be downloaded from here: "https://github.com/tesseract-ocr/tesseract".
