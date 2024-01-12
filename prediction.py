import numpy as np
from PIL import Image
import tensorflow as tf
from keras.utils import img_to_array


img = Image.open("marbel-all/validation_marble/AfyonBeyaz/_273_9556130.jpg")
test_img = img.resize((224,224))
test_img = img_to_array(test_img)
test_img = np.expand_dims(test_img, axis = 0)
img = np.reshape(test_img, (1,224,224,3))

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
# Test the model on random input data.
input_shape = input_details[0]['shape']

interpreter.set_tensor(input_details[0]['index'], img)
interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
output_probs = tf.math.softmax(output_data)
classes_tur = ["AageanRose", "AfyonBal", "AfyonBeyaz", "AfyonBlack", "AfyonGrey", "AfyonSeker", "Bejmermer", "Blue", "Capuchino", "Diyabaz", "DolceVita", "EkvatorPijama", "ElazigVisne", "GoldGalaxy", "GulKurusu", "KaplanPostu", "Karacabeysiyah", "Konglomera", "KristalEmprador", "Leylakmermer", "MediBlack", "OliviaMarble", "Oniks", "RainGrey", "Traverten"]
pred_label = tf.math.argmax(output_probs)
print(output_probs)
max_index = np.argmax(output_probs)
print(max_index)
print(classes_tur[max_index])


