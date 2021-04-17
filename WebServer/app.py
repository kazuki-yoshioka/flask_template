from flask import Flask, render_template, request, jsonify, session, redirect
from datetime import timedelta
from py.controller.ControllerManager import ControllerManager
import os

cM = ControllerManager()
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

    cM = ControllerManager()
    disp = cM.beforeRequest(session, request)
    if ("login" == disp):
        return redirect("/Login")


@app.route('/Login')
def moveLogin():
    """[summary]

    Returns: indexページを表示
        [type]: [description]
    """
    response = cM.execute(session, request)
    session["nextUrl"] = response["nextUrl"]
    session["errMassageList"] = response["errMassageList"]
    # session["response"] = response["response"]

    return render_template(response["nextUrl"] + ".html", model=response["response"])


@app.route('/Enter/<name>/', methods=['GET', 'POST'])
def enter(name=None):
    """[summary]

    Returns: indexページを表示
        [type]: [description]
    """
    response = cM.execute(session, request)
    session["nextUrl"] = response["nextUrl"]
    session["errMassageList"] = response["errMassageList"]
    # session["response"] = response["response"]

    return jsonify({"nextUrl": "login"})


@app.route('/move', methods=['GET', 'POST'])
def move():
    data = request.json
    name = "Good"
    title = "階層チェンジ"
    dict = {name: name, data: data, title: title}
    return render_template("/html/hellow.html", dict=dict)


@app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    _session = cM.execute(session, request)

    return jsonify(_session["response"])


@app.route('/refresh', methods=['GET', 'POST'])
def fetchRefresh():
    data = request.json
    session['userId'] = data['id']
    session['password'] = data['password']
    session['nextUrl'] = '/move'
    dict = {
        'name': data['id'],
        'title': data['password'],
        'nextUrl': data['nextUrl']
    }
    return jsonify(dict)


# 実行
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=5000)
