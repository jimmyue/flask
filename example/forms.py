from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError

class ContactForm(Form):
	name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
	Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
	Address = TextAreaField("Address",[validators.Required("Please enter your Address.")])
	email = TextField("Email",[validators.Email("Please enter your Email.")])
	Age = IntegerField("Age",[validators.Required("Please enter your age.")])
	language = SelectField('Languages', choices = [('cpp', 'C++'), ('py', 'Python')])
	submit = SubmitField("Send")



