from flask import Flask, request, jsonify
import cv2
import pytesseract
import numpy as np

# For this to work, pytesseract executable has to be downloaded from https://github.com/tesseract-ocr/tesseract
# path of pytesseract - change accordingly
pytesseract.pytesseract.tesseract_cmd = r'A:\7\Implementation\Tesseract\tesseract.exe'

app = Flask("__name__")

@app.route('/extract-text', methods=['POST'])
def ocr_image():
    if 'photo' not in request.files:
        return jsonify({"error": "Wrong parameter"}), 400
    
    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({"error": "No photo selected for uploading"}), 400
    
    if photo:
        # OpenCV part
        # Converting the image to a format opencv can understand
        in_memory_file = np.asarray(bytearray(photo.read()), dtype=np.uint8)
        image = cv2.imdecode(in_memory_file, cv2.IMREAD_COLOR)
        
        # Converting image to gray scale (black and white)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Other preprocessing tasks could come here - future improvements
        
        # Tesseract part
        # Using tesseract to do OCR on the processed image
        # Both Hungarian and English texts are recognized
        text = pytesseract.image_to_string(gray_image, lang='hun+eng')
        
        # Return the extracted text as a json response
        return jsonify({"text": text}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)