import datetime
from os import chdir, path
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename

# Dir to save file and history log to
UPLOAD_DIR = r'C:\Users\Student\Databuilder'
chdir(UPLOAD_DIR)

app = Flask(__name__)

app.config['UPLOAD_DIR'] = UPLOAD_DIR

# current post.. placeholder for function
posts = [
    {
        'author': 'Tim Cowan',
        "title": " example title",
        'content': 'first section',
        'date_posted': ' 20191214'

    },
    {
        'author': 'John Doe',
        "title": " example title 2",
        'content': 'first section 2',
        'date_posted': ' 20201214'

    }

]

# Home page using home.html built from layout.html
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

# about.html built from layout.html
@app.route('/about')
def about():
    return render_template('about.html', title="about")

# name to make file association
@app.route("/filedroper", methods=["GET", "POST"])
def username():
    if request.method == "GET":
        return render_template("login.html", title="Upload File")
    if request.method == "POST":
        fileuser = request.form.get('fileuser')
        return redirect(url_for("datadump", name=fileuser))

# select file to upload to flask server
@app.route("/filedrop/<name>", methods=["GET", "POST"])
def datadump(name):
    if request.method == "GET":
        return render_template("basic.html", name=name, title="Upload File")
    if request.method == "POST":
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_DIR'], filename))
            your_time = datetime.datetime.now()
            open("File_History.txt", 'a').write(f"\n{file} Loaded by:{name} at {your_time}")
            return redirect(url_for('username'))
    return


if __name__ == '__main__':
    app.run(debug=True)
