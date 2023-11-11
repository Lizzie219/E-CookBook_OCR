from flask import Flask, request, jsonify
import cv2
import pytesseract
import numpy as np

# path of pytesseract
pytesseract.pytesseract.tesseract_cmd = r'A:\7\Implementation\Tesseract\tesseract.exe'

app = Flask("__name__")

@app.route('/extract-text', methods=['POST'])
def ocr_image():
    if 'photo' not in request.files:
        return jsonify({"error": "No photo part in the request"}), 400
    
    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({"error": "No photo selected for uploading"}), 400
    
    if photo:
        # Convert the image to a format opencv can understand
        in_memory_file = np.asarray(bytearray(photo.read()), dtype=np.uint8)
        image = cv2.imdecode(in_memory_file, cv2.IMREAD_COLOR)
        
        # Convert image to gray scale (optional and can be tuned)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Do preprocessing here (optional, e.g., thresholding, noise removal, etc.)
        
        # Use tesseract to do OCR on the processed image
        text = pytesseract.image_to_string(gray_image, lang='hun+eng')
        
        # Return the extracted text as a json response
        return jsonify({"text": text}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)