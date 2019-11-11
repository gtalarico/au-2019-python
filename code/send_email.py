# import smtplib, ssl

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = "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"

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# #  Test
# mail_from = 'Gui Talarico <"gtalarico@gtalarico.com">'
# mail_to = 'Persio <"talaricotalarico@hotmail.com">'
# mail_from = 'gtalarico@gtalarico.com'
# mail_to = 'gtalarico@gtalarico.com'

# msg = MIMEMultipart()
# msg['From'] = mail_from
# msg['To'] = mail_to
# msg['Subject'] = 'Sending mails with Python'
# mail_body = """
# This is a test.
# """
# msg.attach(MIMEText(mail_body, "plain"))
# try:
#     PORT = 25
#     PORT = 587
#     PORT = 465
#     # server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
#     server = smtplib.SMTP('smtp.sendgrid.net', 587)
#     # server.starttls()
#     # server.ehlo()
#     server.login('apikey', EMAIL_HOST_PASSWORD)
#     server.sendmail(mail_from, mail_to, mail_body)
#     server.close()
#     print("mail sent")
# except Exception as exc:
#     print(exc)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='gtalarico@gtalarico.com',
    to_emails='gtalarico@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
