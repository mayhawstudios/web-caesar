from flask import Flask, request
from caesar import rotate_string

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
    <imput type="text" name="rot" id="rot">
    <textarea>
</form>
"""

page_footer = """
    </body>
</html>
"""

@app.route("/")
def index():
    