import os
import smtplib
import ssl
from email.message import EmailMessage
from typing import List
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("SMTP_SENDER")
PASSWORD = os.getenv("SMTP_PASSWORD")
SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("SMTP_PORT", "465"))
RECIPIENTS = os.getenv("RECIPIENTS",None)
SEND_HOUR = os.getenv("SEND_HOUR","12")
SEND_MINUTES = os.getenv("SEND_MINUTES","25")

if not RECIPIENTS:
    raise ValueError("No receivers set.")
else:
    RECIPIENTS = RECIPIENTS.split(',')

def send_email(to: List[str], subject: str, body: str, *, html: bool = False):
    if not all([SENDER, SERVER, PASSWORD]):
        raise ValueError("Missing SMTP_SENDER, SMTP_SERVER, or SMTP_PASSWORD")

    msg = EmailMessage()
    msg["From"] = SENDER
    msg["To"] = to
    msg["Subject"] = subject

    if html:
        msg.set_content("This email contains HTML.")
        msg.add_alternative(body, subtype="html")
    else:
        msg.set_content(body)

    ctx = ssl.create_default_context()

    if PORT == 465:
        with smtplib.SMTP_SSL(SERVER, PORT, timeout=60, context=ctx) as smtp:
            smtp.login(SENDER, PASSWORD)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(SERVER, PORT, timeout=60) as smtp:
            smtp.ehlo()
            smtp.starttls(context=ctx)
            smtp.ehlo()
            smtp.login(SENDER, PASSWORD)
            smtp.send_message(msg)
