import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = "smtp.gmail.com"
port = 587
username = "sti.erico.matheus@gmail.com"
password = "eytwyoorakmdultg"

mail_from = 'sti.erico.matheus@gmail.com'
mail_subject = "Validation mail Somativa SID"
mail_body = "Please type this number into the system to complete validation."

def sendvalmail(valnum, tomail):
    strvalnum = str(valnum)
    strtomail = str(tomail)
    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = strtomail
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText('Please type this number into the system to complete validation: ' + strvalnum, 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mensagem)
    connection.quit()