from flask import Flask, request,jsonify
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from PIL import Image
from operator import itemgetter
#import hgtk


root_path = "C:/Users/Ai/Desktop/machineGUN/no1/"
root_label_path = root_path + 'first_labels.txt'
f = open(root_label_path, 'r', encoding='utf8')

list_f = f.readlines()

first_labels =[]

for label in list_f:
    first_labels.append(label.strip('\n'))
f.close

interpreter = tf.lite.Interpreter(model_path= root_path+ "model.tflite")
interpreter.allocate_tensors()


def seperate():
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    datagen = ImageDataGenerator(rescale=1. /255)
    test_dir = 'uploaded'
    test_generator = datagen.flow_from_directory(
        test_dir,
        target_size=(224, 224),
        shuffle=False,
        class_mode='categorical',
        batch_size=1)

    input_data = np.array(test_generator[0][0], dtype=np.float32)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])


    print_data =[]
    list_print_data =[]
    for index, value in enumerate(*output_data):
        list_print_data.append([index,value])


    print_data = sorted(list_print_data, key=itemgetter(1), reverse=True)

    result=[]
    #result.append(first_labels[print_data[0][0]])
    for i in range(len(*output_data)):
        result.append(first_labels[print_data[i][0]])

    return str(result[0])

def remo_credir():
    try:
        import shutil
        shutil.rmtree('uploaded/image')
        print()
    except:
        pass

    try:
        os.mkdir('uploaded/image')
    except:
        pass




app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False #jsonify에서 한글 사용 허용
app.config['UPLOAD_FOLDER'] = 'uploaded/image'

@app.route('/API', methods=['POST', 'GET'])
def pred():
    if request.method == 'POST':
        remo_credir()
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        val1 = seperate()
        return jsonify({"result":val1})
    if request.method == 'GET':
        return "get!"

if __name__ == '__main__':
    app.run()
