from flask import Flask, render_template, request, jsonify, send_file, flash, redirect
from final_pipeline import Process_Result
import random
from werkzeug.utils import secure_filename
import os
import pandas as pd
import numpy as np

app = Flask(__name__)
data_model = Process_Result('pipe_model.p') 
UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem' 
app.config['SECRET_KEY'] = 'my key'

@app.route('/')
def index():
    return render_template('index.html')


def solve(filename):
    user_data = pd.read_csv('/tmp/'+filename)  
    data_model.create_pred_df('/tmp/'+filename)
    prediction = data_model.make_new_prediction()  
    prediction = prediction.round(2) 
    return list(prediction) 

@app.route('/download', methods=['GET'])
def download():
    return send_file('green_plan_it_input.csv')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print(request.files)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename.endswith('csv'):
            filename = secure_filename(file.filename + str(random.randint(0,1000000)))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = solve(filename)
            result = {'pred': result}
            return jsonify(result)
                                    

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    ''' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    
