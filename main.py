from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
<form action="/encrypt" method="POST">
    Rotate By :<input type="text" name="rot" id="rot" value="0"><br>
    <textarea name="text">{0}</textarea><br>
    <input type="submit" value="Submit Query">
</form>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = cgi.escape(request.form['text']).strip()

    return form.format(rotate_string(text,rot))

@app.route("/")
def index():
    return form.format("")

app.run()
