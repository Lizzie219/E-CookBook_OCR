import os

import cv2
import numpy as np
import pytesseract
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024


@app.get('/healthz')
def health():
    return jsonify({'status': 'healthy'})


@app.post('/extract-text')
def ocr_image():
    if 'photo' not in request.files:
        return jsonify({'error': 'Wrong parameter'}), 400

    photo = request.files['photo']
    if not photo.filename:
        return jsonify({'error': 'No photo selected for uploading'}), 400

    in_memory_file = np.frombuffer(photo.read(), dtype=np.uint8)
    image = cv2.imdecode(in_memory_file, cv2.IMREAD_COLOR)
    if image is None:
        return jsonify({'error': 'The uploaded file is not a supported image'}), 400

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image, lang='hun+eng')
    return jsonify({'text': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))
