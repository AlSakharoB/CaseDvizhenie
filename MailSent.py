import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def MailCheck(mail, msg):
    if len(mail) == 0:
        return None
    for i in mail:
        if i == '@':
            WriteMail(mail, msg)


def WriteMail(mail, msg_):
    msg = MIMEMultipart()
    msg['From'] = 'Движение'
    msg['To'] = mail
    msg['Subject'] = 'Результат'
    message = msg_
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('dvizheniecase@gmail.com', 'Bot123321')
    mailserver.sendmail('dvizheniecase@gmail.com', mail, msg.as_string())
    print("\033[32m \t{}" .format("Письмо с результатом успешно отправлено"))
    mailserver.quit()