import os
import smtplib
import ssl
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

port = int(os.environ.get('PORT', 465))
smtp_server = os.environ.get('SMTP_SERVER')
sender_email = os.environ.get('SENDER_EMAIL', '<EMAIL>')
receiver_email = os.environ.get('RECEIVER_EMAIL', '<EMAIL>')
password = os.environ.get('SMTP_PASSWORD', '<PASSWORD>')

list_of_addresses = []

message = f"""\
From: michal.sarzala@aluvisagrupo.com
To: {receiver_email}
MIME-Version: 1.0
Content-Type: text/html; charset=utf-8
Subject: Bardzo wazny mail

<h1> Zglaszam rozpoczecie pracy </h1> \n

<b>{datetime.now()}</b>

Pozdrawiam
Michal Sarzala

"""

context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        try:
            server.starttls(context=ssl.create_default_context())
        except smtplib.SMTPNotSupportedError:
            print('SMTP server not support ssl')
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
except TimeoutError:
    print('SMTP server timed out')
except Exception as e:
    print(f'Error: {e}')
