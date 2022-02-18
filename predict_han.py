#from flask import Flask, request,jsonify
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from operator import itemgetter
#import app
import hgtk


def hangeul(label):
    root_path = "C:\\Users\\Ai\\Desktop\\han\\" +str(label) + "\\"
    root_label_path = root_path + 'labels.txt'
    f = open(root_label_path, 'r', encoding='utf8')

    list_f = f.readlines()

    first_labels =[]

    for label in list_f:
        first_labels.append(label.strip('\n'))
    f.close

    interpreter = tf.lite.Interpreter(model_path= root_path+ "model.tflite")
    interpreter.allocate_tensors()
    
    return interpreter, first_labels

def seperate(num, interpreter,first_labels):
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        datagen = ImageDataGenerator(rescale=1. /255)
        test_dir = 'C:/Users/Ai/Desktop/final_cut'
        test_generator = datagen.flow_from_directory(
            test_dir,
            target_size=(300,300),
            shuffle=False,
            class_mode='categorical',
            batch_size=1)

        input_data = np.array(test_generator[num][0], dtype=np.float32)

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
        result.append(first_labels[print_data[0][0]])

        if result[0] == 'x':
            return None
        else:
            return result[0]   

def start_han(num):
    combine_text = []
    label_list = ['first', 'middle', 'last']
    for han in range(0, 3):
        inter,first_labels = hangeul(label_list[han])
        combine_text.append(seperate(num, inter, first_labels))
    answer = hgtk.letter.compose(*combine_text)

    return str(answer)
