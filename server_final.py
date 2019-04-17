import flask
from flask import flash
from flask import render_template
import io
import tensorflow as tf
import base64
from yolo import YOLO
from PIL import Image

#Start Flask App
app = flask.Flask(__name__)
app.secret_key = 'mensajes de error'

#Class instance
detector = YOLO()


def StartModel():
    global model
    global graph
    graph = tf.get_default_graph()

StartModel()

@app.route("/")
def Start():
    return render_template("form.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Dict with predictions
	data = {"success": False}

	# Check the image
	if flask.request.method == "POST":
		if flask.request.files.get("image"):
			# Read image in PIL fortmat
			image = flask.request.files["image"].read()
			imagePred = Image.open(io.BytesIO(image))
			with graph.as_default():
				pred=detector.detect_image(imagePred)
				prediction=pred[0]
				imagePredicted=pred[1]
				img_io = io.BytesIO()
				imagePredicted.save(img_io, 'PNG', quality=100)
				img_io.seek(0)
				img = base64.b64encode(img_io.getvalue())
				final_image = img.decode('ascii')
				data={'preds':prediction,'imagen':final_image}

			# Return the result with the data
			return render_template("result.html",data=data)

		else:
			flash('Por favor, selecciona una imagen')
			return render_template("result.html")

# Start the app
if __name__ == "__main__":
	print(("*Loading keras...."))







