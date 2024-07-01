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


@app.route('/get_image_process', methods=['GET'])
def get_image():
	return jsonify({"get_image_success": "Image Success"})


@app.route('/hello_world', methods=['GET'])
def get_hello_word():
	return jsonify({"hello_world": "Hello World"})

@app.route('/hello_iko', methods=['GET'])
def get_hello_iko():
	return jsonify({"hello_iko": "Hello Iko"})

@app.route('/hello', methods=['GET'])
def get_hello():
	return jsonify({"hello": "Hello"})

@app.route('/fizz_buzz', methods=['GET'])
def get_fizz_buzz():
	data = []
	parameter = request.args.get('length', default=1, type=int)
	for i in range (1, int(parameter)+1):
		data1 = i % 3 == 0 and i % 5 == 0
		data2 = i % 3 == 0
		data3 = i % 5 == 0
		if data1:
			result = f"FizzBuzz {i}"
			data.append(result)
		elif data2:
			result = f"Fizz {i}"
			data.append(result)
		elif data3:
			result = f"Buzz {i}"
			data.append(result)
		else:
			data.append(i)
	return jsonify({"data": data})


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

