import smtplib
from email.mime.text import MIMEText

sender = 'timothym@3dservices.co.ug'
receiver = 'masikotimo@gmail.com'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'timothym@3dservices.co.ug'
msg['To'] = 'masikotimo@gmail.com'

user = 'timothym@3dservices.co.ug'
password = '.Forward2021'

server = smtplib.SMTP_SSL("mail.3dservices.co.ug",465)
server.login(user, password)
server.sendmail(sender, receiver, msg.as_string())
print("mail successfully sent")





