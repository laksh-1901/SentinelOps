import smtplib
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_RECEIVER


def send_email(subject, message):
    email = EmailMessage()

    email["Subject"] = subject
    email["From"] = EMAIL_ADDRESS
    email["To"] = EMAIL_RECEIVER

    email.set_content(message)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email)
