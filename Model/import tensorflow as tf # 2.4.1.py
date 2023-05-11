import tensorflow as tf # 2.4.1 
from tensorflow.keras.models import load_model




interpreter = tf.lite.Interpreter(model_path = 'C:/Users/alaak/Desktop/Old.tflite')
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print("Input Shape:", input_details[0]['shape'])
print("Input Type:", input_details[0]['dtype'])
print("Output Shape:", output_details[0]['shape'])
print("Output Type:", output_details[0]['dtype'])