import sqlite3 as sql
from flask import Flask, render_template,request
app =Flask(__name__)

def Createdb():
	conn = sqlite3.connect('./static/database.db')
	print("Opened database successfully")
	conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
	print("Table created successfully")
	conn.close()

@app.route('/')
def home():
	return render_template('sql_home.html')

@app.route('/enternew')
def new_student():
	return render_template('sql_student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			nm = request.form['nm']
			addr = request.form['add']
			city = request.form['city']
			pin = request.form['pin']
			with sql.connect("./static/database.db") as con:
				con.execute("INSERT INTO students (name,addr,city,pin) VALUES ('%s','%s','%s','%s')" % (nm,addr,city,pin))
				con.commit()
				msg = "Record successfully added"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("sql_result.html",msg = msg)
			con.close()

@app.route('/list')
def list():
	con = sql.connect("./static/database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from students")
	rows = cur.fetchall(); 
	return render_template("sql_list.html",rows = rows)

if __name__ == '__main__':
	app.run(debug = True)