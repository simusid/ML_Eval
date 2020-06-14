from flask import Flask
from flask import render_template
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'h5'}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./uploads"

# serve static text
@app.route('/')
def hello_world():
    return 'Hello, World!'

# ensure templates work
@app.route("/main")
@app.route("/main/<name>")
def main(name=None):
    return render_template("main.html", name=name)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("*********", url_for("uploaded_file", filename=filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route("/uploaded_file/<filename>")
def uploaded_file(filename=None):
   return render_template("uploaded_file.html", filename=filename)
