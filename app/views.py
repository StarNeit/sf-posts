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

@app.route('/success_oauth_mission', methods=['GET'])
def success_oauth():
    if request.method == 'GET':
        code = request.args.get('code')
        p = requests.post("https://stackexchange.com/oauth/access_token/json", {'client_id': 11134, 'code': code, 'redirect_uri': 'https://radiant-springs-83002.herokuapp.com/success_oauth_mission', 'client_secret': 'zrMV6ym0MSYNynpNkz9*vQ(('})
        token = json.loads(p.text)['access_token']
        r = requests.get("https://api.stackexchange.com/2.2/me?key=bltjJ8PWcScpa5ORgXSBBA((&site=stackoverflow&order=desc&sort=reputation&access_token="+token+"&filter=default")
        id = json.loads(r.text)['items'][0]['user_id']
        res = requests.get("http://api.stackexchange.com/2.2/users/"+str(id)+"/posts?order=desc&sort=activity&site=stackoverflow")
        data = json.loads(res.text)
        return render_template('success_oauth.html', data=data['items'])