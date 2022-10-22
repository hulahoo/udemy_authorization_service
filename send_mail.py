"""
Примеры отрпавки сообщения
"""
# 1
import smtplib
import ssl
import logging
from email.mime.text import MIMEText


async def send_email(
        *,
        email: str,
        subject: str,
        text: str
):
    msg = MIMEText(text)

    MAIL_FROM = "youremail@gmail.com"
    MAIL_PASSWORD = "your password"
    msg["Subject"] = subject
    msg["From"] = MAIL_FROM
    msg["To"] = email
    MAIL_SERVER = "smtp.mail.ru"
    MAIL_PORT = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(MAIL_SERVER, MAIL_PORT, context=context) as server:
        server.login(MAIL_FROM, MAIL_PASSWORD)
        server.sendmail(MAIL_FROM, email, msg.as_string())
        logging.info(f"Email to {email} sent")

# 2
from django.core.mail import send_mail
send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)

# 3
"""
Сервис mailjet. Можно найти примеры по ссылке https://github.com/mailjet/mailjet-apiv3-python
"""
