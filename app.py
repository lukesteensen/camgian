import sqlite3
from os import environ
from flask import Flask, request, make_response, redirect, render_template, url_for, g


app = Flask(__name__)
app.debug = True


def connect_db():
    return sqlite3.connect("data.db")


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        resp = make_response(redirect(url_for('locations_index')))
        resp.set_cookie('user', request.form['user'])
        return resp
    else:
        return render_template("login.html")


@app.route('/logout', methods=["GET"])
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('user', expires=0)
    return resp


@app.route('/locations')
def locations_index():
    # user = request.cookies.get('user')
    cur = g.db.execute("select * from locations;")
    locations = [dict(id=row[0], name=row[1]) for row in cur.fetchall()]
    return render_template("locations.html", locations=locations)


@app.route('/location/<int:id>')
def location(id):
    location = locations[id]
    return render_template('location.html', location=location)


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

