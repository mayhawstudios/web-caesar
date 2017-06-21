from flask import Flask, request
from caesar import rotate_string

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
<form action="/cypher" method="POST">
    <label for="rot">Rotate By:</label>
    <imput type="text" name="rot" id="rot" value="0">
    <textarea name="text">
    <imput type="submit" value="Submit Query">
</form>
"""

page_footer = """
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    return False

@app.route("/")
def index():
    form = page_header + cypher_form + page_footer
    return form

app.run()
