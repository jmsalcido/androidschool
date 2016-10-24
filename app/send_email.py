from app import app, mail

from flask_mail import Message
from flask import render_template
from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()

def send_confirmation_email(email_to, confirmation_url):
    email_html = render_template('user/confirmation.html', confirmation_url=confirmation_url)
    send_email("Confirmation email for Android School",
               "admin@nearsoft.com", [email_to], email_html, email_html)
