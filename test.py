from flask import Flask
from Home import Home

app = Flask(__name__)

@app.route('/')
def hello_world():
    home = Home()
    return home.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
