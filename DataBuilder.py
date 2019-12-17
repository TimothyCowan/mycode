#!/usr/bin/python3
from os import chdir, path
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from werkzeug.utils import secure_filename
import datetime

# Directory to save upload to
UPLOAD_DIR = r'C:\Users\Student\Databuilder'
# AUTH_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'yaml'}
# Change cwd
chdir(r'C:\Users\Student\Databuilder')

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR


@app.route("/filedroper", methods=["GET", "POST"])
def username():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        fileuser = request.form.get('fileuser')
        return redirect(url_for("datadump", name=fileuser))


@app.route("/filedrop/<name>", methods=["GET", "POST"])
def datadump(name):
    if request.method == "GET":
        return render_template("basic.html", name=name)
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

# fileuser = autherizied users in list.. check against that list

# add a user to auth list

#


if __name__ == '__main__':
    app.run(debug=True)
