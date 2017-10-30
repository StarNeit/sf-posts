from flask import render_template, redirect, url_for, request
import requests, json

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success_basic_mission', methods = ['POST'])
def success_basic():
    if request.method == 'POST':
        r = requests.get("http://api.stackexchange.com/2.2/users/"+request.form.get('id')+"/posts?order=desc&sort=activity&site=stackoverflow")
        data = json.loads(r.text)

        return render_template('success_basic.html', data = data['items'])

@app.route('/success_oauth_mission', methods=['POST'])
def success_oauth():
    if request.method == 'POST':
        p = requests.post("https://stackexchange.com/oauth/access_token/json", {'client_id': 11134, 'code': 'oyQ39Uxiu7xeD3bjxnT02Q))', 'redirect_uri': 'https://radiant-springs-83002.herokuapp.com', 'client_secret': 'zrMV6ym0MSYNynpNkz9*vQ(('})
        r = requests.get(
            "http://api.stackexchange.com/2.2/users/"+request.form.get('id')+"/posts?order=desc&sort=activity&site=stackoverflow&token="+json.loads(p.text)['access_token']+"&key=bltjJ8PWcScpa5ORgXSBBA((")

        data = json.loads(r.text)

        return render_template('success_oauth.html', data=data['items'])