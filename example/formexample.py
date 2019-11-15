from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError
app = Flask(__name__)
app.secret_key = 'development key'

class ContactForm(Form):
	name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
	Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
	Address = TextAreaField("Address",[validators.Required("Please enter your Address.")])
	email = TextField("Email",[validators.Email("Please enter your Email.")])
	Age = IntegerField("Age",[validators.Required("Please enter your age.")])
	language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])
	submit = SubmitField("Send")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form = form)
		else:
			return '<h1>Form posted successfully</h1>'
	elif request.method == 'GET':
		return render_template('contact.html', form = form)

if __name__ == '__main__':
	app.run(debug = True)
