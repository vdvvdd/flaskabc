from flask import Flask 
from flask import request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hello', methods=['POST'])
def hello_post():
    return 'Hello, World(post)'

@app.route('/user/<username>')
def user_id(username):
    return 'hello ' + username 

@app.route('/query')
def query():
    name = request.args.get('name')
    return 'hello, ' + name 

@app.route('/query_url')
def query_url():
    return 'query_url: ' + url_for('query')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
