import smtplib, ssl
from email.message import EmailMessage
from login import *

sender = sender
password = mpassword
receiver = receiver

password = 'xlrgcccfuvleusyw'
receiver = 'akashkmore2002@gmail.com'
def send_mail():
    body_msg = f'''Subject: How to send emails with python
    I learnet to sned email with python with easy method.
    '''
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, body_msg)

def send_contact_mail(cname, cemail, subject, message):
    body_msg = f'''
    Client Name:- {cname}
    Client Email:- {cemail}
    Message:- {message}
    '''
    msg = EmailMessage()
    msg['Subject'] = f'{cname} contacted regarding {subject}'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body_msg)
  
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)

def send_service_mail(oname, oemail, jname, jlocation, jdesc):
    body_msg = f'''
    Organization:- {oname}
    Organization Email:- {oemail}
    Job/ Work:- {jname}
    Location:- {jlocation}
    Work Description:- {jdesc}
    '''
    msg = EmailMessage()
    msg['Subject'] = f'{oname} want to hire you..'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body_msg)
  
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)