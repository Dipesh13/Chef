from flask import Flask, request, send_file
from werkzeug import secure_filename
import os
from xml_test import parse
app = Flask(__name__)


@app.route("/ocr", methods=["POST"])
def ocr():
    file= request.files['file']
    filename = secure_filename(file.filename)
    file.save(filename
    return parse(filename[0:-4])
    # return filename, send_file(filename, mimetype= 'json')

if __name__ == '__main__':
    app.run(debug=True)
