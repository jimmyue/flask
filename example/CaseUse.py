import os
from flask import Flask, render_template, request ,make_response, session, redirect, url_for, escape, abort, flash
from werkzeug import secure_filename
app = Flask(__name__)

#静态JS
@app.route("/js")
def index():
	return render_template("index.html")


#form
@app.route('/')
def student():
	return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template("result.html",result = result)


#cookies
@app.route('/cookies')
def index_cookies():
	return render_template('getcookies.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
	if request.method == 'POST':
		user = request.form['nm']
		resp = make_response(render_template('readcookies.html'))
		resp.set_cookie('userID', user)
	return resp

@app.route('/getcookie')
def getcookie():
	name = request.cookies.get('userID')
	return '<h1>welcome %s </h1>' % name


#Sessions
app.secret_key = 'any random string'

@app.route('/session')
def sessions_index():
	if 'username' in session:
		username=session['username']
		return render_template("session_notlogin.html",username = username)
	return render_template("session_logged.html")

@app.route('/login', methods = ['GET', 'POST'])
def sessions_login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('sessions_index'))
	return render_template("session_login.html")

@app.route('/logout')
def sessions_logout():
	session.pop('username', None)
	return redirect(url_for('sessions_index'))


#重定向和错误
@app.route('/redirect')
def redirect_index():
	return render_template('redirect_login.html')

@app.route('/redirectlogin',methods = ['POST', 'GET'])
def redirect_login():
	if request.method == 'POST':
		if request.form['username'] == 'admin' :
			return redirect(url_for('redirect_success'))
		else:
			abort(401)
	else:
		return redirect(url_for('redirect_index'))

@app.route('/redirectsuccess')
def redirect_success():
	return 'logged in successfully'


#消息闪现
#flash(message, category)
#get_flashed_messages(with_categories, category_filter)
@app.route('/message')
def message_index():
	return render_template('message_index.html')

@app.route('/message_login', methods = ['GET', 'POST'])
def message_login():
	error = None

	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid username or password. Please try again!'
		else:
			flash('You were successfully logged in')
			return redirect(url_for('message_index'))
	return render_template('message_login.html', error = error)


#文件上传
app.config['UPLOAD_FOLDER']='./static'
@app.route('/upload')
def upload():
	return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return 'file uploaded successfully'


if __name__ == '__main__':
	app.run(host='127.0.0.1',port='5000',debug=True)