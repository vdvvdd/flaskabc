from flask import Flask 
from flask import request 
from flask import render_template 
from flask import redirect

app = Flask(__name__)

@app.route("/user", methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        if username=='daihao' and password=='123456':
            return redirect("https://www.google.com.hk/")
        else:
            message = "login failed"
            return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')