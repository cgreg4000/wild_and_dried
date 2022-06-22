from flask_app import app
from flask import render_template, redirect, request
import smtplib

@app.route('/')
def main():

    return render_template('index.html')

@app.route('/gallery')
def gallery():


    return render_template('gallery.html')

@app.route('/markets')
def markets():


    return render_template('markets.html')

@app.route('/contact')
def contact():


    return render_template('contact.html')

@app.route('/contact_process', methods=['POST'])
def process():

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'phone' : request.form['phone'],
        'category' : request.form['category'],
        'message' : request.form['message'],
    }

    def message(data):
        return f"First Name - {data['first_name']} || Last Name - {data['last_name']} || Email - {data['email']} || Phone - {data['phone']} || Category - {data['category']} || Message - {data['message']}"
        

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('email.com', 'password')
    server.sendmail('email', 'email', message(data))


    return redirect('/')
