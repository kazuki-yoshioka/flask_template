from flask import Flask, render_template, request, jsonify, session, redirect
from datetime import timedelta
from py.controller import controllerManager
from py.model import baseModel
import os


cM = controllerManager.controllerManager()
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.before_request
def make_session_permanent():
    """[summary]
        リクエストの初期処理
    Returns:
        [type]: [description]
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

    cM = controllerManager.controllerManager()
    disp = cM.beforeRequest(session, request)
    if("login" == disp):
        return redirect("http://localhost:5000/")


@app.route('/')
def index():
    """[summary]

    Returns: indexページを表示
        [type]: [description]
    """
    cM.execute(session, request)

    dict = {"name": "name", "title": "title"}
    return render_template("index.html", dict=dict)


@ app.route('/move', methods=['GET', 'POST'])
def move():
    data = request.json
    name = "Good"
    title = "階層チェンジ"
    dict = {name: name, data: data, title: title}
    return render_template("/html/hellow.html", dict=dict)


@ app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    _session = cM.execute(session, request)

    return jsonify(_session["response"])


@ app.route('/refresh', methods=['GET', 'POST'])
def fetchRefresh():
    data = request.json
    session['userId'] = data['id']
    session['password'] = data['password']
    session['nextUrl'] = '/move'
    dict = {'name': data['id'], 'title': data['password'],
            'nextUrl': data['nextUrl']}
    return jsonify(dict)


# 実行
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=5000)