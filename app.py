# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import find_pos
import cut_img
import what_img
import file_read
import predict_num
import predict_han
import os

app = Flask(__name__)



@app.route('/img_model_page/')
def hello_world():
    return render_template('img_model_page.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['input_img']
        f.save('C:/Users/Ai/Desktop/save_img/success_img/' + secure_filename(f.filename))
        a = 'C:/Users/Ai/Desktop/save_img/success_img/' + secure_filename(f.filename)
        cut_img.path_what(a)

        final_answer = ''
        b = file_read.file_read()
        for re in range(0, b):
            if what_img.seperate(re) == 'model_han':
                #한글실행
                final_answer += predict_han.start_han(re)
            elif what_img.seperate(re) == 'model_number':
                #final_answer += '숫자'
                final_answer += predict_num.seperate(re)

        return render_template('img_model_page.html', final_answer=final_answer)
        #val1 = seperate()
        #return jsonify({"result":val1})
        #return str(cut_img.path_what(a))
        #return str(find_pos.position_num(str(a)))
        #return render_template('img_model_page.html')

if __name__ == '__main__':
    app.run(debug = True)
