from flask import Flask, render_template, request, redirect, send_file
from models import File
import os
p =  os.path.abspath("app.py")
i = p.index("app.py")
p = p[:i] + "files"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = p
app.config['SECRET_KEY'] = 'aoaaoaoaoaoaoaaoaoaoaooaaoa'



@app.route('/add', methods = ['POST'])
def AddFile():
	f = request.files['file']
	n = f.filename
	f.save(os.path.join(app.config['UPLOAD_FOLDER'],n))
	fl = File(name = n)
	fl.save()
	return "ok"


@app.route('/')
def index():
	files = File.select()
	return render_template("index.html", files = files)

@app.route('/del/<id>')
def Del(id):
	fl = File.get(File.id == id)
	fl.delete_instance()
	return "ok"

@app.route('/download/<name>')
def Download(name):
	addr = "files/" + name
	return send_file(addr)