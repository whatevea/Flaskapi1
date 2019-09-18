#C:\Users\DELL\Desktop>
from flask import Flask
app= Flask(__name__)
@app.route('/')
def nulljson():
	return "NO request"
@app.route('/anime/<string:name>',methods=['POST'])
def findallepisode():
	pass
