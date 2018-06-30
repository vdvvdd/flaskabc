from flask import Flask 
from flask import request 
from flask import render_template 
from flask import redirect

app = Flask(__name__)

from wtforms import Form, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])

@app.route("/user", methods=['GET', 'POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        if username=='daihao' and password=='123456':
            return redirect("https://www.google.com.hk/")
        else:
            message = "login failed"
            return render_template('index.html', form=myForm, message=message)

    return render_template('index.html', form=myForm)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')