from flask import Flask
from flask import render_template
from models import User


app = Flask(__name__)


@app.route('/')
def hello():
    content = 'hello vdvvdd'
    return render_template('index.html', content=content) 

@app.route('/user')
def user_index():
    user = User(1, 'king') 
    return render_template('user_index.html', user=user) 


@app.route('/user/<userid>')
def query_user(userid):
    user = None 
    if int(userid) == 1:
        user = User(1, 'james')

    return render_template('user_id.html', user=user) 

@app.route('/users')
def user_list():
    users = [] 
    for i in range(1, 11):
        user = User(i, 'kobe(' + str(i) + ')')
        users.append(user)

    return render_template('user_list.html', users=users) 

@app.route('/one')
def base_one():
    return render_template('base_one.html')

@app.route('/two')
def base_two():
    return render_template('base_two.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
