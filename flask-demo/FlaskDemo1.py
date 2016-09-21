from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'username %s' % username


@app.route('/post/<int:post_id>')
def show_post_id(post_id):
    return 'post_id %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'method is post.'
    else:
        return 'method is get.'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


def log_the_user_in(param):
    pass


def valid_login(username, password):
    if username=='kevin'and password=='123456':
        return True
    else:
        return False


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['usernmae'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'invalid username/password.'
        return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
