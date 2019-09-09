from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

encrypt_form = """
<!doctype html>
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
        <title>Caesar Encryption</title>
    </head>
    <body>
        <form method="POST">
            <label>
                Rotate by:
                <input type="text" name="rot" value="0">
            </label>
            <label>
                <textarea name="text">{0}</textarea>
            </label>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return encrypt_form.format('')

@app.route('/', methods=['POST'])
def encryption():
    rotate=request.form['rot']
    entered=request.form['text']
    encrypted_text=encrypt(entered,rotate)
    
    return encrypt_form.format(encrypted_text)

app.run()