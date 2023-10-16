from flask import Flask, render_template, request, redirect, session, flash
import os
from db import Database
from api import API

app = Flask(__name__)
app.secret_key = os.urandom(24)
dbo = Database()
apio = API()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')

    else:
        return redirect('/')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('login_email')
    password = request.form.get('login_password')

    users = dbo.select(email, password)

    if len(users) > 0:
        session['user_id'] = users[0][0]

        return redirect('/home')

    else:
        flash('Invalid Email ID or Password !!')

        return redirect('/')

@app.route('/add_user', methods=['POST'])
def add_user():
    name =request.form.get('signup_name')
    email = request.form.get('signup_email')
    password = request.form.get('signup_password')

    response = dbo.insert(name, email, password)

    if response:
        flash('Registration Successful !!')

        return redirect('/')

    else:
        flash('Email ID already exists !!')

        return redirect('/signup')

@app.route('/ner')
def ner():
    if 'user_id' in session:
        return render_template('ner.html')

    else:
        return redirect('/')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    text = request.form.get('ner_text')

    response = apio.ner(text)

    return render_template('ner.html', response=response, text=text)

@app.route('/sa')
def sa():
    if 'user_id' in session:
        return render_template('sa.html')

    else:
        return redirect('/')

@app.route('/perform_sa', methods=['POST'])
def perform_sa():
    text = request.form.get('sa_text')

    response = apio.sa(text)

    return render_template('sa.html', response=response, text=text)

@app.route('/acc')
def acc():
    if 'user_id' in session:
        return render_template('acc.html')

    else:
        return redirect('/')

@app.route('/perform_acc', methods=['POST'])
def perform_acc():
    text = request.form.get('acc_text')

    response = apio.acc(text)

    return render_template('acc.html', response=response, text=text)

@app.route('/logout')
def logout():
    flash('You\'ve been logged out !!')

    session.pop('user_id')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)