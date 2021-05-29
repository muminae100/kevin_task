from flask import render_template,redirect,request,url_for,flash,abort
from app import app,mail
from app.forms import RequestQuoteForm
from flask_mail import Message



def send_email(email,message,phonenumber,fullname):
    msg = Message(f'Email from {email}, phone number: {phonenumber}', 
                   sender=email,
                   recipients=['smuminaetx100@gmail.com'])
    msg.body = f'''
Company name/Individual: {fullname}
{message}
'''
    mail.send(msg)

@app.route('/')
def index():
    form = RequestQuoteForm()
    if form.validate_on_submit():
        send_email(email=form.email.data,phonenumber=form.phonenumber.data,fullname=form.fullname.data)
    return render_template('index.html', form = form)

@app.route('/about_us')
def about():
    return render_template('about_us.html', title='About us')

@app.route('/our_products_&_services')
def products():
    return render_template('our_products&services.html', title='Our products and services')

@app.route('/contact_us')
def contact():
    return render_template('contact_us.html', title='Contact us')