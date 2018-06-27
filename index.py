from flask import Flask 
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    msg = 'backend message'
    return render_template('index.html', message=msg)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

