from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    #msg = 'backend message'
    if request.method == 'POST':
        a = request.form['add1']
        b = request.form['add2']
        a = int(a)
        b = int(b)
        ret = a + b
        return render_template('index.html', message=ret)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

