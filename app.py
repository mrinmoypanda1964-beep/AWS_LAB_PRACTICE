from flask import Flask
app = Flask(__Panda__)

@app.route('/')
def hello():
    return "Hello from Flask on Amplify!"
