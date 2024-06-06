from flask import Flask, request, jsonify, send_file
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"})

    file = request.files['image']
    img = Image.open(file.stream)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

    _, img_encoded = cv2.imencode('.png', gray_img)
    img_bytes = BytesIO(img_encoded.tobytes())

    return send_file(img_bytes, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
