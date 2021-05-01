from flask import Flask, render_template, request, jsonify, session, redirect, make_response
from datetime import timedelta
from py.controller.ControllerManager import ControllerManager
import os
from flask_cors import CORS

cM = ControllerManager()
app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)


@app.before_request
def make_session_permanent():
    """[summary]
        リクエストの初期処理
    Returns:
        [type]: [description]
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

    cM = ControllerManager()
    disp = cM.beforeRequest(session, request)
    if ("Login" == disp):
        return redirect("/Login")


@app.route('/Login')
def moveLogin():
    """[summary]

    Returns: indexページを表示
        [type]: [description]
    """
    response = cM.execute(session, request)
    session["response"] = response["nextUrl"]
    #session["errMassageList"] = response["errMassageList"]
    # session["response"] = response["response"]

    return render_template(response["nextUrl"] + ".html", model=response)


@app.route('/Enter/<path1>/', methods=['GET', 'POST'])
@app.route('/Enter/<path1>/<path2>/', methods=['GET', 'POST'])
def enter(path1=None, path2=None):
    """[summary]

    Returns: indexページを表示
        [type]: [description]
    """
    response = cM.execute(session, request)
    session["response"] = response
    session["model"] = response["model"]
    session["userId"] = response["userId"]
    # session["model"] = response["model"]

    dict = response
    return jsonify(dict)


@app.route('/Move/<path1>/', methods=['GET', 'POST'])
@app.route('/Move/<path1>/<path2>/', methods=['GET', 'POST'])
def move(path1=None, path2=None):
    #nextUrl = "/" + path + ".html"
    nextUrl = "/Menu/Menu.html"
    return render_template(nextUrl, model=session["model"])


@app.route('/fetch', methods=['GET', 'POST'])
def fetch():
    #_session = cM.execute(session, request)
    dict = {
        'name': 'name',
        'title': 'title',
        'nextUrl': 'nextUrl'
    }
    return jsonify(dict)


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
