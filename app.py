from os import environ
from flask import Flask, request, make_response, redirect, render_template, url_for


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    user = request.cookies.get('username')
    if not user:
        return redirect(url_for('login'))
    else:
        return 'hello' + user


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('username', request.form['username'])
        return resp
    else:
        return render_template("index.html")


@app.route('/logout', methods=["GET"])
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('username', expires=0)
    return resp


if __name__ == '__main__':
    port  = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

