from flask import Flask,render_template,request,url_for,redirect
import mysql.connector
app = Flask(__name__)

conn = mysql.connector.connect(host="localhost",user="root",password="",database="auth")
curr = conn.cursor()

@app.route('/login')
@app.route('/')
def hellow():
    return render_template('login.html')


@app.route('/register.html')
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home.html')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login_validation',methods=['POST','GET'])
def login_validation():
    id = request.form.get('id')
    password = request.form.get('password')

    curr.execute("""SELECT *FROM `entry` WHERE `id` LIKE '{}' AND `password` LIKE '{}'""".format(id,password))
    users = curr.fetchall() #it return the list inside to tuple
    if len(users)>0:
        return redirect('/home')      #redirect used for after comming to dashboard login validation function is trigger continously
    else:
        return redirect('/login')  



@app.route('/add_user.html',methods=['POST','GET'])
@app.route('/add_user',methods=['POST','GET'])
def add_user():
    name = request.form.get('name')
    id = request.form.get('id')
    password = request.form.get('password')
    curr.execute("""INSERT INTO `entry` (`name`,`id`,`password`) VALUES ('{}','{}','{}')""".format(name,id,password))
    conn.commit()          #relation databases for data intigriy managagment
    return "Register sucessfully"



if __name__:"__main__"
app.run(debug=True)
