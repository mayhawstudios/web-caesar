from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
 """
cypher_form = """
<form action="/encrypt" method="POST">
    Rotate By :<input type="text" name="rot" id="rot" value="0"><br>
    <textarea name="text">
    </textarea><br>
    <input type="submit" value="Submit Query">
</form>
<p name="error"></p>
"""

page_footer = """
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    plaintext = request.form['text'].strip()

    if type(int(rot)) != int:
        error = "You must input a valid number."

        return redirect("/?error=" + error)

    if plaintext.strip() == "":
        error = "You cannot leave text blank."

        return redirect("/?error=" + error)
    else:
        rot = int(rot)

        return rotate_string(plaintext,rot)

@app.route("/")
def index():
    # if we have an error, make a <p> to display it
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p>' + error_esc + '</p>'
    else:
        error_element = ''

    form = page_header + cypher_form + page_footer
    return form

app.run()
