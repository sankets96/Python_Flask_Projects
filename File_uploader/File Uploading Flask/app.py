from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
path_file = 'D:\\File Uploading Flask\\static>'  #upload location
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'



if __name__ == '__main__':
   app.run(debug=True)