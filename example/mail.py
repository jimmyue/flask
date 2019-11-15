from flask import Flask,render_template, request
from flask_mail import Mail, Message

app =Flask(__name__)

app.config['MAIL_SERVER']='smtp.263.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cmssystem@way-s.cn'
app.config['MAIL_PASSWORD'] = 'cms#2018!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route("/")
def index():
	msg = Message('Hello', sender = 'cmssystem', recipients = ['yuejing@way-s.cn'])
	msg.body = "Hello Flask message sent from Flask-Mail"
	mail.send(msg)
	return "Sent"

if __name__ == '__main__':
	app.run(debug = True)