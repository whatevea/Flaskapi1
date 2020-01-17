#C:\Users\DELL\Desktop>
from flask import Flask,Response,request,jsonify
import requests
app= Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	q=request.args.get('q')
	headers={'Referer': 'http://vidstreaming.io', 'TE': 'Trailers', 'Alt-Used': 'vidstreaming.io:443', 'X-Requested-With': 'XMLHttpRequest'}
	r=requests.get('http://vidstreaming.io/ajax-search.html?keyword='+q,headers=headers).text
	modified=r.replace("/videos/","/watchanime.html?q=/videos/")
	return jsonify(modified)	
@app.route('/')
def nulljson():
	return q
@app.route('/asd')
def findallepisode(name):
	headers={'Referer': 'http://vidstreaming.io', 'TE': 'Trailers', 'Alt-Used': 'vidstreaming.io:443', 'X-Requested-With': 'XMLHttpRequest'}
	r=requests.get('http://vidstreaming.io/ajax-search.html?keyword='+name,headers=headers).json()
	return r
