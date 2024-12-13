from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

SUBJECTS = ["Basic Electrical Engineering", "Math", "Physics", "PPS", "Indian Constitution (IC)"]

@app.route('/')
def index():
    return render_template('index.html', subjects=SUBJECTS)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        subject = request.form['subject']
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload.html', subjects=SUBJECTS)

@app.route('/view/<subject>')
def view(subject):
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('view.html', subject=subject, files=files)

if __name__ == '__main__':
    app.run(debug=True)
