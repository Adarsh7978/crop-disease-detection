import numpy as np
from PIL import Image
import tensorflow as tf

model = tf.lite.Interpreter(model_path="model/model.tflite")
model.allocate_tensors()

async def predict_image(file):
    image = Image.open(file.file).resize((224, 224))
    img = np.array(image) / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)

    input_details = model.get_input_details()
    output_details = model.get_output_details()

    model.set_tensor(input_details[0]['index'], img)
    model.invoke()
    output = model.get_tensor(output_details[0]['index'])

    labels = open("model/labels.txt").read().splitlines()
    return labels[np.argmax(output)]
