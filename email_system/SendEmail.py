import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def sendEmailToClient(name, email):
    subject = "3D Services "
    body = """Hello %s,\n\n You are going to get deactivated soon Kindly renew your subscription package """ % (
        name)

    sender_email = "masiko@3dservices.co.ug"
    receiver_email = email
    password = "huRGUBT#D1Ro"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    server = smtplib.SMTP_SSL("mail.3dservices.co.ug", 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    server.quit()


def sendEmailToCMS(name, email, people):
    sender_email = "masiko@3dservices.co.ug"
    receiver_email = email
    password = "huRGUBT#D1Ro"

    msg = MIMEMultipart()

    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = '3D Services'

    text = """Hello %s,\n\n The Following are subscription are soon getting blocked, Please get in touch with them """ % (
        name)
    html = """\
        <html>
            <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->

        </head>
            <body>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


            <table class="table table-bordered" border="1">

                <thead class="thead-dark">
                <tr>
                    <th scope="col">Name of client</th>
                    <th scope="col">Email Address</th>
                    
                </tr>
                </thead>
                <tbody>""" + "".join(
        ["<tr><th>{0}</th><td>{1}</td></tr>".format(a, k) for a, k in people.items()]) + """</tbody></table>
                </body></html>"""
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP_SSL("mail.3dservices.co.ug", 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
