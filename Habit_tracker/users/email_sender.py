
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, recipient):
    """
    Отправляет электронное письмо с указанными параметрами.
    subject - тема письма
    body - текст письма
    recipient - адрес получателя
    """
    sender = "habit.tracker@yandex.com"  # почта приложения Бекхана
    password = "atzcmytorzngapay"  # пароль от почты приложения Бекхана

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    body_part = MIMEText(body)
    message.attach(body_part)

    with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, message.as_string())


def Approving_mail(username, email, url):
    subject = "Подтверждение электронной почты"
    body = f"Уважаемый/ая {username},\nМы получили запрос на подтверждение адреса электронной почты {email}.\nПожалуйста, нажмите на ссылку ниже для подтверждения:\n{url}\nЕсли вы не запрашивали подтверждение, пожалуйста, проигнорируйте это сообщение.\nС уважением,Команда поддержки"
    recipient = email
    send_email(subject, body, recipient)
    return


def dayly_remember(username, email):
    subject = "Ты сможешь!"
    body = f"Салам {username}\nДавай ты сможешь"
    recipient = email
    send_email(subject, body, recipient)


# Approving_mail('Bekhan', 'bekhan@duck.com', 'url')
# dayly_remember('Bekhan', 'bekhan@duck.com')
